import unittest
from datetime import date, datetime, timezone

from scripts.dashboard_refresh import build_dataset, validate_dataset


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
        data = build_dataset(None, None, date(2026, 9, 1), date(2026, 9, 2), self.now)
        with self.assertRaisesRegex(ValueError, "stale_reporting_period"):
            validate_dataset(data, today=date(2026, 10, 29))


if __name__ == "__main__":
    unittest.main()
