import requests
from api_practice.config_util import get_base_url, get_timeout

def send_request(request_data):
    response = requests.request(
        method=request_data.get("method"),
        url = get_base_url().rstrip("/") + "/" + request_data["url"].lstrip("/"),
        json=request_data.get("json"),
        headers=request_data.get("headers"),
        params=request_data.get("params"),
        data=request_data.get("data"),
        timeout=get_timeout(),
    )
    return response
