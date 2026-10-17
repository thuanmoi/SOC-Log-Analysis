#!/usr/bin/env python3
"""Analyze simulated CSV network-flow records."""
import argparse
import csv
from collections import Counter, defaultdict
import sys

REQUIRED = {"timestamp", "src_ip", "dst_ip", "dst_port", "protocol", "action"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csvfile")
    args = parser.parse_args()
    denied_by_source = Counter()
    ports_by_pair = defaultdict(set)
    rows = 0
    try:
        with open(args.csvfile, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
                raise ValueError("CSV is missing required columns")
            for row in reader:
                rows += 1
                if row["action"].upper() == "DENY":
                    denied_by_source[row["src_ip"]] += 1
                    ports_by_pair[(row["src_ip"], row["dst_ip"])].add(row["dst_port"])
    except (OSError, ValueError, csv.Error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Records analyzed: {rows}")
    for ip, count in denied_by_source.most_common():
        print(f"DENIED CONNECTIONS: src_ip={ip} count={count}")
    for (src, dst), ports in ports_by_pair.items():
        if len(ports) >= 4:
            print(f"REVIEW: src_ip={src} dst_ip={dst} distinct_denied_ports={len(ports)}")
    if not denied_by_source:
        print("No denied connections in dataset.")

if __name__ == "__main__":
    main()
