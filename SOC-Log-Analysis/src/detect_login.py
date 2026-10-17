#!/usr/bin/env python3
"""Detect repeated failed logins followed by a success in a time window.

Input is a synthetic, line-oriented authentication log. Standard library only.
This is a learning example, not a production detection system.
"""
from collections import defaultdict, deque
from datetime import datetime, timedelta
import re
import sys

PATTERN = re.compile(
    r"^(?P<ts>\S+) user=(?P<user>\S+) src_ip=(?P<ip>\S+) event=(?P<event>\S+)$"
)

def parse_line(line):
    match = PATTERN.match(line.strip())
    if not match:
        return None
    item = match.groupdict()
    try:
        item["ts"] = datetime.fromisoformat(item["ts"].replace("Z", "+00:00"))
    except ValueError:
        return None
    return item

def detect(lines, threshold=3, window_minutes=5):
    failures = defaultdict(deque)
    alerts = []
    window = timedelta(minutes=window_minutes)
    for line_number, line in enumerate(lines, start=1):
        event = parse_line(line)
        if not event:
            continue
        key = (event["user"], event["ip"])
        if event["event"] == "login_failed":
            q = failures[key]
            q.append(event["ts"])
            while q and event["ts"] - q[0] > window:
                q.popleft()
        elif event["event"] == "login_success":
            q = failures[key]
            while q and event["ts"] - q[0] > window:
                q.popleft()
            if len(q) >= threshold:
                alerts.append({
                    "user": event["user"],
                    "src_ip": event["ip"],
                    "failed_attempts": len(q),
                    "success_time": event["ts"].isoformat(),
                    "line": line_number,
                })
            q.clear()
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
