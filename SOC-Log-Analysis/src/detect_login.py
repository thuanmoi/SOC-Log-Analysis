#!/usr/bin/env python3
"""Detect repeated failed logins followed by a success within a time window.

Input is a synthetic, line-oriented authentication log. Standard library only.
This is a learning example, not a production detection system.
"""
from collections import defaultdict, deque
from datetime import datetime, timedelta
import math
import re
import sys

PATTERN = re.compile(
    r"^(?P<ts>\S+) user=(?P<user>\S+) src_ip=(?P<ip>\S+) event=(?P<event>\S+)$"
)
SUPPORTED_EVENTS = {"login_failed", "login_success"}


def parse_line(line):
    """Parse one log line; return None for malformed or unsupported events."""
    match = PATTERN.match(line.strip())
    if not match:
        return None
    item = match.groupdict()
    try:
        timestamp = datetime.fromisoformat(item["ts"].replace("Z", "+00:00"))
    except ValueError:
        return None
    # Require timezone-aware timestamps so mixed local/UTC values cannot crash
    # comparisons or silently produce misleading time-window results.
    if timestamp.utcoffset() is None or item["event"] not in SUPPORTED_EVENTS:
        return None
    item["ts"] = timestamp
    return item


def detect(lines, threshold=3, window_minutes=5):
    """Return alerts for failures followed by success for the same user/IP.

    Events are processed chronologically. Original line numbers are retained
    for traceability. Threshold and window must be positive.
    """
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        raise ValueError("threshold must be a positive integer")
    try:
        valid_window = (
            isinstance(window_minutes, (int, float))
            and not isinstance(window_minutes, bool)
            and window_minutes > 0
            and math.isfinite(float(window_minutes))
        )
    except (OverflowError, ValueError):
        valid_window = False
    if not valid_window:
        raise ValueError("window_minutes must be a finite positive number")
    try:
        window = timedelta(minutes=window_minutes)
    except OverflowError:
        raise ValueError("window_minutes is too large") from None

    parsed_events = []
    for line_number, line in enumerate(lines, start=1):
        event = parse_line(line)
        if event:
            parsed_events.append((event["ts"], line_number, event))

    parsed_events.sort(key=lambda row: (row[0], row[1]))
    failures = defaultdict(deque)
    alerts = []

    for timestamp, line_number, event in parsed_events:
        key = (event["user"], event["ip"])
        attempts = failures[key]

        while attempts and timestamp - attempts[0] > window:
            attempts.popleft()

        if event["event"] == "login_failed":
            attempts.append(timestamp)
        elif event["event"] == "login_success":
            if len(attempts) >= threshold:
                alerts.append({
                    "user": event["user"],
                    "src_ip": event["ip"],
                    "failed_attempts": len(attempts),
                    "success_time": timestamp.isoformat(),
                    "line": line_number,
                })
            attempts.clear()

    return alerts


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "logs/sample_auth.log"
    try:
        with open(path, encoding="utf-8") as handle:
            alerts = detect(handle)
    except OSError as exc:
        print(f"Error reading log: {exc}", file=sys.stderr)
        raise SystemExit(1)

    if not alerts:
        print("No matching patterns detected.")
        return

    print(f"Alerts found: {len(alerts)}")
    for alert in alerts:
        print(
            "SUSPICIOUS_LOGIN user={user} src_ip={src_ip} "
            "failed_attempts={failed_attempts} success_time={success_time} "
            "line={line}".format(**alert)
        )


if __name__ == "__main__":
    main()
