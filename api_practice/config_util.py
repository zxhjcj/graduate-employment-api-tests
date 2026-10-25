import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CASE_FILE = BASE_DIR / "config.yaml"
def read_config():
    with open(CASE_FILE, encoding="utf-8") as f:
        cases = yaml.safe_load(f) or []
        return cases

def get_base_url():
    config = read_config()
    return config["base_url"]

def get_timeout():
    config = read_config()
    return config["timeout"]
