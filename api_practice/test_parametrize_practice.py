import pytest

from api_practice.request_util import send_request
from api_practice.util_yaml import read_test_config
from api_practice.assert_util import assert_validate

@pytest.mark.parametrize("case_data", read_test_config())
def test_login(case_data):
    request_data = case_data["request"]
    validate_data = case_data["validate"]
    response = send_request(request_data)
    assert_validate(response, validate_data)




