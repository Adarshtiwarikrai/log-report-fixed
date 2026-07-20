import hashlib
import json
from pathlib import Path


REPORT = Path("/app/report.json")
ACCESS_LOG = Path("/app/access.log")
# Expected SHA-256 of the shipped /app/access.log (criterion 5).
EXPECTED_ACCESS_LOG_SHA256 = (
    "e83c0cb8dd9c33cbe0954cc038bd0ff90834cf48747e257d931dce5b2408d38e"
)


def test_report_exists_and_valid_json():
    """Success criterion 1: /app/report.json exists and is valid JSON."""
    assert REPORT.exists(), "no /app/report.json found"
    json.loads(REPORT.read_text())


def test_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty log lines."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IPs."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequent request path (/index.html)."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"


def test_access_log_unmodified():
    """Success criterion 5: /app/access.log must not be modified."""
    digest = hashlib.sha256(ACCESS_LOG.read_bytes()).hexdigest()
    assert digest == EXPECTED_ACCESS_LOG_SHA256
