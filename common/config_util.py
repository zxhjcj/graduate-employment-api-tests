import os
from pathlib import Path

import yaml


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config.yaml"


def read_config():
    with open(CONFIG_FILE, encoding="utf-8", mode="r") as f:
        return yaml.safe_load(f) or {}


def get_env():
    config = read_config()
    return os.getenv("TEST_ENV") or config.get("env", "dev")


def get_env_config():
    config = read_config()
    env = get_env()
    env_config = config.get(env)
    if not env_config:
        raise KeyError(f"config.yaml 中不存在环境配置: {env}")
    return env_config


def get_base_url():
    return os.getenv("BASE_URL") or get_env_config()["base_url"].rstrip("/")


def get_timeout():
    return get_env_config().get("timeout", 10)
