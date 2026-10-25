import pytest

from api_practice.util_yaml import read_test_config
from request_util import send_request
from assert_util import assert_validate

@pytest.mark.parametrize("case", read_test_config(),ids=[case["name"] for case in read_test_config()])
def test_get_profile(token, case):
    request_data = case["request"]
    request_data["headers"]["Authorization"] = f"Bearer {token}"

    response = send_request(request_data)

    validate_data = case["validate"]
    assert_validate(response, validate_data)


