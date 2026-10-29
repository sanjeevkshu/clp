#!/usr/bin/env python3
"""Fetch and validate a privacy-safe, aggregate-only public dashboard dataset."""
from __future__ import annotations

import json
import math
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
MIN_COHORT = 10
ALLOWED_TOP = {"schema_version", "generated_at_utc", "reporting_period", "sources", "metrics", "limitations"}
ALLOWED_SOURCES = {"ga4", "search_console"}
ALLOWED_METRICS = {
    "active_users", "sessions", "engagement_rate", "average_engagement_time_seconds",
    "organic_clicks", "search_impressions", "search_ctr", "average_position"
}
FORBIDDEN_KEY = re.compile(r"(email|name|user.?id|client.?id|session.?id|cookie|token|secret|query|ip.?address|form|raw|payload|stack)", re.I)
DEFAULT_LIMITATIONS = [
    "Only aggregate totals are published; no user-level records or query-level search terms are exposed.",
    "Search Console data may be delayed. Reporting periods use completed dates.",
    "Low-volume GA4 totals are suppressed when active users are fewer than 10."
]


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def validate_dataset(data: Any, *, today: date | None = None) -> None:
    if not isinstance(data, dict) or set(data) != ALLOWED_TOP:
        raise ValueError("top_level_schema")
    if data["schema_version"] != SCHEMA_VERSION:
        raise ValueError("schema_version")
    try:
        generated = datetime.fromisoformat(data["generated_at_utc"].replace("Z", "+00:00"))
        start = date.fromisoformat(data["reporting_period"]["start_date"])
        end = date.fromisoformat(data["reporting_period"]["end_date"])
    except (AttributeError, KeyError, TypeError, ValueError):
        raise ValueError("date_format") from None
    if set(data["reporting_period"]) != {"start_date", "end_date"}:
        raise ValueError("reporting_period_schema")
    if generated.tzinfo is None or end < start or end > (today or date.today()):
        raise ValueError("date_order")
    if (today or date.today()) - end > timedelta(days=14):
        raise ValueError("stale_reporting_period")
    if set(data["sources"]) != ALLOWED_SOURCES or not isinstance(data["metrics"], dict):
        raise ValueError("source_or_metrics_schema")
    if set(data["metrics"]) - ALLOWED_METRICS:
        raise ValueError("unknown_metric")
    for source in data["sources"].values():
        if not isinstance(source, dict) or set(source) != {"status", "label"}:
            raise ValueError("source_schema")
        if source["status"] not in {"available", "suppressed", "unavailable"}:
            raise ValueError("source_status")
        if not isinstance(source["label"], str) or len(source["label"]) > 80:
            raise ValueError("source_label")
    for key, value in data["metrics"].items():
        if FORBIDDEN_KEY.search(key) or isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("metric_type")
        if not math.isfinite(value) or value < 0 or (key in {"engagement_rate", "search_ctr"} and value > 1):
            raise ValueError("metric_range")
    if not isinstance(data["limitations"], list) or any(not isinstance(x, str) or len(x) > 240 for x in data["limitations"]):
        raise ValueError("limitations_schema")
    serialized = json.dumps(data, ensure_ascii=True)
    if re.search(r"https?://[^\s\"']+[?#][^\s\"']*", serialized, re.I):
        raise ValueError("unsafe_url")


def build_dataset(ga4_values: dict[str, float] | None, gsc_values: dict[str, float] | None,
                  start: date, end: date, generated: datetime | None = None) -> dict[str, Any]:
    metrics: dict[str, float] = {}
    ga4_status = "unavailable"
    if ga4_values is not None:
        users = ga4_values.get("active_users", 0)
        if users < MIN_COHORT:
            ga4_status = "suppressed"
        else:
            ga4_status = "available"
            metrics.update({k: float(v) for k, v in ga4_values.items()
                            if k in {"active_users", "sessions", "engagement_rate", "average_engagement_time_seconds"}})
    gsc_status = "unavailable"
    if gsc_values is not None:
        gsc_status = "available"
        metrics.update({k: float(v) for k, v in gsc_values.items()
                        if k in {"organic_clicks", "search_impressions", "search_ctr", "average_position"}})
    data = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": (generated or utc_now()).isoformat().replace("+00:00", "Z"),
        "reporting_period": {"start_date": start.isoformat(), "end_date": end.isoformat()},
        "sources": {
            "ga4": {"status": ga4_status, "label": "Google Analytics 4"},
            "search_console": {"status": gsc_status, "label": "Google Search Console"}
        },
        "metrics": metrics,
        "limitations": DEFAULT_LIMITATIONS
    }
    validate_dataset(data)
    return data


def fetch_and_build() -> dict[str, Any]:
    import google.auth
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest
    from googleapiclient.discovery import build

    # Use the same completed 28-day window for both providers; Search Console has a longer delay.
    end = date.today() - timedelta(days=3)
    start = end - timedelta(days=27)
    credentials, _ = google.auth.default(scopes=[
        "https://www.googleapis.com/auth/analytics.readonly",
        "https://www.googleapis.com/auth/webmasters.readonly"
    ])
    ga4_client = BetaAnalyticsDataClient(credentials=credentials)
    ga4_response = ga4_client.run_report(RunReportRequest(
        property=f"properties/{os.environ['GA4_PROPERTY_ID']}",
        date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
        metrics=[Metric(name="activeUsers"), Metric(name="sessions"),
                 Metric(name="engagementRate"), Metric(name="averageEngagementTime")],
        limit=1
    ))
    ga4_values = None
    if ga4_response.rows:
        row = ga4_response.rows[0]
        values = [float(x) for x in row.metric_values]
        ga4_values = {
            "active_users": values[0], "sessions": values[1],
            "engagement_rate": values[2], "average_engagement_time_seconds": values[3]
        }
    # Search Console is queried only for aggregate totals; no query/page dimensions.
    gsc_end = end
    gsc_start = start
    gsc = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
    response = gsc.searchanalytics().query(
        siteUrl=os.environ["GSC_SITE_URL"],
        body={"startDate": gsc_start.isoformat(), "endDate": gsc_end.isoformat(), "rowLimit": 1}
    ).execute()
    gsc_values = None
    rows = response.get("rows", [])
    if rows:
        row = rows[0]
        gsc_values = {
            "organic_clicks": float(row.get("clicks", 0)),
            "search_impressions": float(row.get("impressions", 0)),
            "search_ctr": float(row.get("ctr", 0)),
            "average_position": float(row.get("position", 0))
        }
    # Use the older of the two source windows for clear, comparable period metadata.
    return build_dataset(ga4_values, gsc_values, gsc_start, gsc_end)


def main() -> int:
    output = Path(os.environ.get("DASHBOARD_OUTPUT", "dashboard-data.json"))
    try:
        data = fetch_and_build()
        output.write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
        print("Dashboard candidate validated; public metric values are not logged.")
        return 0
    except Exception as exc:
        # Fail with a stable category only. Never emit provider payloads or exception text.
        category = "configuration_or_api_failure"
        if isinstance(exc, ValueError):
            category = str(exc) if re.fullmatch(r"[a-z_]+", str(exc)) else "schema_validation"
        print(f"::error::Dashboard refresh failed at stage: {category}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
