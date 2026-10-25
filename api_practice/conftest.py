import pytest
from request_util import send_request
from assert_util import assert_validate
@pytest.fixture(scope="session")
def token():
    request_data = {
        "method": "POST",
        "url": "/api/auth/login",
        "json": {
            "username": "stu001",
            "password": "123456",
        },
    }
    validate_data = [
        {"eq": ["status_code", 200]},
        {"eq": ["body.code", 200]},
        {"not_null": ["body.data.token"]},
    ]
    response = send_request(request_data)
    assert_validate(response, validate_data)
    body = response.json()
    token_value = body["data"]["token"]
    return token_value


