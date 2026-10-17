import math
import unittest

from detect_login import detect, parse_line


def event(ts, user="alice", ip="192.0.2.10", kind="login_failed"):
    return f"{ts} user={user} src_ip={ip} event={kind}"


class DetectionTests(unittest.TestCase):
    def test_three_failures_then_success_within_window_alerts(self):
        lines = [
            event("2026-10-01T09:30:01Z"),
            event("2026-10-01T09:30:04Z"),
            event("2026-10-01T09:30:07Z"),
            event("2026-10-01T09:30:10Z", kind="login_success"),
        ]
        alerts = detect(lines)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["user"], "alice")
        self.assertEqual(alerts[0]["failed_attempts"], 3)

    def test_two_failures_do_not_alert(self):
        lines = [
            event("2026-10-01T09:30:01Z"),
            event("2026-10-01T09:30:04Z"),
            event("2026-10-01T09:30:10Z", kind="login_success"),
        ]
        self.assertEqual(detect(lines), [])

    def test_old_failures_expire_from_window(self):
        lines = [
            event("2026-10-01T09:00:01Z"),
            event("2026-10-01T09:01:02Z"),
            event("2026-10-01T09:02:03Z"),
            event("2026-10-01T09:10:04Z", kind="login_success"),
        ]
        self.assertEqual(detect(lines), [])

    def test_failures_from_different_users_are_not_combined(self):
        lines = [
            event("2026-10-01T09:30:01Z", user="alice"),
            event("2026-10-01T09:30:02Z", user="bob"),
            event("2026-10-01T09:30:03Z", user="alice"),
            event("2026-10-01T09:30:04Z", kind="login_success", user="alice"),
        ]
        self.assertEqual(detect(lines), [])

    def test_failures_from_different_ips_are_not_combined(self):
        lines = [
            event("2026-10-01T09:30:01Z", ip="192.0.2.10"),
            event("2026-10-01T09:30:02Z", ip="192.0.2.11"),
            event("2026-10-01T09:30:03Z", ip="192.0.2.12"),
            event("2026-10-01T09:30:04Z", ip="192.0.2.10", kind="login_success"),
        ]
        self.assertEqual(detect(lines), [])

    def test_malformed_line_is_ignored(self):
        self.assertIsNone(parse_line("not-a-valid-log-line"))
        self.assertEqual(detect(["not-a-valid-log-line"]), [])

    def test_invalid_timestamp_is_ignored(self):
        line = "not-a-date user=alice src_ip=192.0.2.10 event=login_failed"
        self.assertIsNone(parse_line(line))

    def test_timezone_naive_timestamp_is_ignored(self):
        line = "2026-10-01T09:30:01 user=alice src_ip=192.0.2.10 event=login_failed"
        self.assertIsNone(parse_line(line))

    def test_unknown_event_type_is_ignored(self):
        line = event("2026-10-01T09:30:01Z", kind="password_reset")
        self.assertIsNone(parse_line(line))

    def test_out_of_order_input_is_processed_chronologically(self):
        lines = [
            event("2026-10-01T09:30:10Z", kind="login_success"),
            event("2026-10-01T09:30:07Z"),
            event("2026-10-01T09:30:04Z"),
            event("2026-10-01T09:30:01Z"),
        ]
        alerts = detect(lines)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["line"], 1)

    def test_custom_threshold_can_be_used(self):
        lines = [
            event("2026-10-01T09:30:01Z"),
            event("2026-10-01T09:30:02Z"),
            event("2026-10-01T09:30:03Z", kind="login_success"),
        ]
        self.assertEqual(len(detect(lines, threshold=2)), 1)

    def test_invalid_threshold_and_window_raise_value_error(self):
        with self.assertRaises(ValueError):
            detect([], threshold=0)
        for invalid_window in (0, -1, math.inf, -math.inf, math.nan):
            with self.subTest(window_minutes=invalid_window):
                with self.assertRaises(ValueError):
                    detect([], window_minutes=invalid_window)


if __name__ == "__main__":
    unittest.main(verbosity=2)
