#!/usr/bin/env python3
"""Flag simple review candidates in synthetic network-flow CSV data.

Learning example only. A flagged row is not proof of malicious activity.
"""
import csv
import sys

BYTE_REVIEW_THRESHOLD = 5_000_000
CONNECTION_REVIEW_THRESHOLD = 10


def analyze(path):
    findings = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row_number, row in enumerate(csv.DictReader(handle), start=2):
            try:
                byte_count = int(row["bytes"])
                connections = int(row["connection_count"])
            except (KeyError, ValueError):
                continue

            # Negative byte or connection counts are invalid flow data.
            if byte_count < 0 or connections < 0:
                continue

            reasons = []
            if byte_count >= BYTE_REVIEW_THRESHOLD:
                reasons.append("high_bytes")
            if connections >= CONNECTION_REVIEW_THRESHOLD:
                reasons.append("many_connections")
            if reasons:
                findings.append({
                    "row": row_number,
                    "src_ip": row.get("src_ip", "unknown"),
                    "dst_ip": row.get("dst_ip", "unknown"),
                    "reasons": ",".join(reasons),
                    "bytes": byte_count,
                    "connection_count": connections,
                })
    return findings


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/sample_flows.csv"
    try:
        findings = analyze(path)
    except OSError as exc:
        print(f"Error reading flow data: {exc}", file=sys.stderr)
        raise SystemExit(1)

    print(f"Rows flagged for review: {len(findings)}")
    for item in findings:
        print(
            "REVIEW row={row} src_ip={src_ip} dst_ip={dst_ip} "
            "reasons={reasons} bytes={bytes} connections={connection_count}"
            .format(**item)
        )


if __name__ == "__main__":
    main()
