import csv
import os
import tempfile
import unittest

from analyze_flows import analyze


class AnalyzeFlowsTests(unittest.TestCase):
    def write_csv(self, rows):
        handle = tempfile.NamedTemporaryFile(
            mode="w", newline="", encoding="utf-8", suffix=".csv", delete=False
        )
        self.addCleanup(lambda: os.path.exists(handle.name) and os.unlink(handle.name))
        with handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "timestamp", "src_ip", "dst_ip", "dst_port",
                    "protocol", "bytes", "packets", "connection_count",
                ],
            )
            writer.writeheader()
            writer.writerows(rows)
        return handle.name

    def row(self, *, bytes_value="1000", connections="1",
            src_ip="192.0.2.10", dst_ip="198.51.100.20"):
        return {
            "timestamp": "2026-10-01T09:00:00Z",
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "dst_port": "443",
            "protocol": "TCP",
            "bytes": bytes_value,
            "packets": "10",
            "connection_count": connections,
        }

    def test_flags_high_byte_count_at_threshold(self):
        path = self.write_csv([self.row(bytes_value="5000000")])
        findings = analyze(path)
        self.assertEqual(len(findings), 1)
        self.assertIn("high_bytes", findings[0]["reasons"])

    def test_flags_connection_count_at_threshold(self):
        path = self.write_csv([self.row(connections="10")])
        findings = analyze(path)
        self.assertEqual(len(findings), 1)
        self.assertIn("many_connections", findings[0]["reasons"])

    def test_includes_both_reasons_when_both_thresholds_are_met(self):
        path = self.write_csv([self.row(bytes_value="5000000", connections="10")])
        findings = analyze(path)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["reasons"], "high_bytes,many_connections")

    def test_does_not_flag_values_below_thresholds(self):
        path = self.write_csv([self.row(bytes_value="4999999", connections="9")])
        self.assertEqual(analyze(path), [])

    def test_skips_missing_or_non_integer_numeric_values(self):
        path = self.write_csv([
            self.row(bytes_value="", connections="10"),
            self.row(bytes_value="5000000", connections="not-a-number"),
            self.row(bytes_value="1000", connections="1"),
        ])
        self.assertEqual(analyze(path), [])

    def test_skips_negative_byte_or_connection_counts(self):
        path = self.write_csv([
            self.row(bytes_value="-1", connections="10"),
            self.row(bytes_value="5000000", connections="-1"),
            self.row(bytes_value="-1", connections="-1"),
        ])
        self.assertEqual(analyze(path), [])

    def test_preserves_source_row_number_and_addresses(self):
        path = self.write_csv([
            self.row(bytes_value="1000"),
            self.row(bytes_value="6000000", src_ip="192.0.2.25",
                     dst_ip="198.51.100.80"),
        ])
        findings = analyze(path)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["row"], 3)
        self.assertEqual(findings[0]["src_ip"], "192.0.2.25")
        self.assertEqual(findings[0]["dst_ip"], "198.51.100.80")


if __name__ == "__main__":
    unittest.main(verbosity=2)
