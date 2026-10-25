import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXTRACT_FILE = BASE_DIR / "extract.yaml"

def read_yaml():
    with open(EXTRACT_FILE, encoding="utf-8", mode="r") as f:
        return yaml.safe_load(f) or {}

def write_yaml(data):
    old_data = read_yaml()
    old_data.update(data)
    with open(EXTRACT_FILE, encoding="utf-8", mode="w") as f:
        yaml.safe_dump(old_data, stream=f, allow_unicode=True)

def clear_yaml():
    with open(EXTRACT_FILE, encoding="utf-8", mode="w") as f:
        yaml.safe_dump({}, stream=f, allow_unicode=True)

def read_textCase(file_path):
    case_file = BASE_DIR / file_path
    with open(case_file, encoding="utf-8", mode="r") as f:
        return yaml.safe_load(f) or {}
# if __name__ == "__main__":
#     data = read_yaml()
#     print(data)
#     write_yaml()

