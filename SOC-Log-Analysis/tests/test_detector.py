from datetime import datetime
import unittest
from detect_login import detect


def event(ts, user="alice", ip="192.0.2.10", kind="login_failed"):
    return f"{ts} user={user} src_ip={ip} event={kind}"


class DetectionTests(unittest.TestCase):
    def test_three_failures_then_success_within_window_alerts(self):
        lines = [event("2026-10-01T09:30:01Z"), event("2026-10-01T09:30:04Z"), event("2026-10-01T09:30:07Z"), event("2026-10-01T09:30:10Z", kind="login_success")]
        self.assertEqual(len(detect(lines)), 1)

    def test_two_failures_do_not_alert(self):
        lines = [event("2026-10-01T09:30:01Z"), event("2026-10-01T09:30:04Z"), event("2026-10-01T09:30:10Z", kind="login_success")]
        self.assertEqual(detect(lines), [])

    def test_old_failures_expire_from_window(self):
        lines = [event("2026-10-01T09:00:01Z"), event("2026-10-01T09:01:02Z"), event("2026-10-01T09:02:03Z"), event("2026-10-01T09:10:04Z", kind="login_success")]
        self.assertEqual(detect(lines), [])

    def test_failures_from_different_users_are_not_combined(self):
        lines = [event("2026-10-01T09:30:01Z"), event("2026-10-01T09:30:02Z", user="bob"), event("2026-10-01T09:30:03Z"), event("2026-10-01T09:30:04Z", kind="login_success")]
        self.assertEqual(detect(lines), [])

    def test_malformed_line_is_ignored(self):
        self.assertEqual(detect(["not-a-valid-log-line"]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
