import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_FILE = BASE_DIR / "test_fixture_practice.yaml"


def read_test_config():
    with open(CASE_FILE, encoding="utf-8") as f:
        cases = yaml.safe_load(f) or []
    return cases