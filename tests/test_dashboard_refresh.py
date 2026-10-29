import unittest
from datetime import date, datetime, timezone

from scripts.dashboard_refresh import (average_engagement_time_seconds, build_dataset,
                                         safe_api_category, validate_dataset)


class EngagementMetricTests(unittest.TestCase):
    def test_average_engagement_time_uses_active_users(self):
        self.assertEqual(average_engagement_time_seconds(120.0, 10.0), 12.0)

    def test_average_engagement_time_handles_zero_active_users(self):
        self.assertEqual(average_engagement_time_seconds(120.0, 0.0), 0.0)


class DashboardDiagnosticTests(unittest.TestCase):
    def test_api_statuses_map_to_safe_categories(self):
        class FakeApiError(Exception):
            def __init__(self, code):
                self.code = code
        self.assertEqual(safe_api_category(FakeApiError(400)), "bad_request_or_invalid_property")
        self.assertEqual(safe_api_category(FakeApiError(401)), "unauthenticated")
        self.assertEqual(safe_api_category(FakeApiError(403)), "permission_denied_or_api_disabled")
        self.assertEqual(safe_api_category(FakeApiError(404)), "property_or_resource_not_found")
        self.assertEqual(safe_api_category(FakeApiError(429)), "quota_exceeded")
        self.assertEqual(safe_api_category(FakeApiError(503)), "provider_unavailable")

    def test_unknown_api_error_does_not_expose_exception_text(self):
        class FakeApiError(Exception):
            pass
        error = FakeApiError("contains private provider response")
        self.assertEqual(safe_api_category(error), "api_error")
        self.assertNotIn("private", safe_api_category(error))


class DashboardDatasetTests(unittest.TestCase):
    def setUp(self):
        self.start = date(2026, 10, 1)
        self.end = date(2026, 10, 28)
        self.now = datetime(2026, 10, 29, tzinfo=timezone.utc)

    def test_low_volume_ga4_is_suppressed(self):
        data = build_dataset(
            {"active_users": 9, "sessions": 12, "engagement_rate": 0.5, "average_engagement_time_seconds": 15},
            {"organic_clicks": 20, "search_impressions": 100, "search_ctr": 0.2, "average_position": 4},
            self.start, self.end, self.now
        )
        self.assertEqual(data["sources"]["ga4"]["status"], "suppressed")
        self.assertNotIn("active_users", data["metrics"])
        self.assertIn("organic_clicks", data["metrics"])

    def test_valid_aggregate_passes(self):
        data = build_dataset(
            {"active_users": 10, "sessions": 15, "engagement_rate": 0.4, "average_engagement_time_seconds": 20},
            {"organic_clicks": 4, "search_impressions": 30, "search_ctr": 0.1, "average_position": 5},
            self.start, self.end, self.now
        )
        validate_dataset(data, today=date(2026, 10, 29))

    def test_unknown_top_level_key_fails_closed(self):
        data = build_dataset(None, None, self.start, self.end, self.now)
        data["unexpected"] = "no"
        with self.assertRaisesRegex(ValueError, "top_level_schema"):
            validate_dataset(data, today=date(2026, 10, 29))

    def test_unknown_metric_fails_closed(self):
        data = build_dataset(None, None, self.start, self.end, self.now)
        data["metrics"]["email_count"] = 1
        with self.assertRaisesRegex(ValueError, "unknown_metric"):
            validate_dataset(data, today=date(2026, 10, 29))

    def test_impossible_metric_range_fails(self):
        data = build_dataset(None, None, self.start, self.end, self.now)
        data["metrics"]["engagement_rate"] = 1.5
        with self.assertRaisesRegex(ValueError, "metric_range"):
            validate_dataset(data, today=date(2026, 10, 29))

    def test_stale_period_fails(self):
        with self.assertRaisesRegex(ValueError, "stale_reporting_period"):
            build_dataset(None, None, date(2026, 9, 1), date(2026, 9, 2), self.now)

    def test_non_finite_metric_fails(self):
        data = build_dataset(None, None, self.start, self.end, self.now)
        data["metrics"]["sessions"] = float("nan")
        with self.assertRaisesRegex(ValueError, "metric_range"):
            validate_dataset(data, today=date(2026, 10, 29))

    def test_extra_reporting_period_field_fails(self):
        data = build_dataset(None, None, self.start, self.end, self.now)
        data["reporting_period"]["extra"] = "no"
        with self.assertRaisesRegex(ValueError, "reporting_period_schema"):
            validate_dataset(data, today=date(2026, 10, 29))


if __name__ == "__main__":
    unittest.main()
