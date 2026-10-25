import requests

from common.config_util import get_base_url, get_timeout
from common.logger_util import get_logger
from common.yaml_util import read_yaml


class TestAPI:
    sess = requests.Session()
    logger = get_logger("request")

    @classmethod
    def replace_extract_value(cls, data):
        extract_data = read_yaml()
        if isinstance(data, dict):
            return {key: cls.replace_extract_value(value) for key, value in data.items()}
        if isinstance(data, list):
            return [cls.replace_extract_value(item) for item in data]
        if isinstance(data, str) and data.startswith("${") and data.endswith("}"):
            key = data[2:-1]
            if key not in extract_data:
                raise KeyError(f"extract.yaml 中不存在变量: {key}")
            return extract_data[key]
        if isinstance(data, str):
            for key, value in extract_data.items():
                data = data.replace("${" + key + "}", str(value))
            return data
        return data

    @classmethod
    def build_url(cls, url):
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return get_base_url() + "/" + url.lstrip("/")

    @classmethod
    def send_all_requests(cls, method, url, **kwargs):
        method = method.upper()
        url = cls.build_url(url)
        cls.logger.info("发送请求: %s %s", method, url)
        try:
            res = cls.sess.request(method=method, url=url, **kwargs)
        except requests.exceptions.Timeout as e:
            raise RuntimeError(f"请求超时: {method} {url}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"请求失败: {method} {url}, 原因: {e}") from e

        cls.logger.info("响应结果: status_code=%s, body=%s", res.status_code, res.text)
        return res

    @classmethod
    def send_case_request(cls, case_data):
        request_data = cls.replace_extract_value(case_data["request"])
        return cls.send_all_requests(
            method=request_data["method"],
            url=request_data["url"],
            headers=request_data.get("headers"),
            params=request_data.get("params"),
            json=request_data.get("json"),
            data=request_data.get("data"),
            timeout=request_data.get("timeout", get_timeout()),
        )
