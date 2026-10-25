def get_value(response, check_key):
    if check_key == "status_code":
        return response.status_code

    if check_key.startswith("body."):
        value = response.json()
        for key in check_key.split(".")[1:]:
            value = value[key]
        return value

    raise KeyError(f"不支持的校验字段: {check_key}")

def assert_validate(response, validate_data):
    for validate in validate_data:
        if "eq" in validate:
            check_key, expected = validate["eq"]
            assert get_value(response, check_key) == expected
        elif "not_null" in validate:
            check_key = validate["not_null"][0]
            assert get_value(response, check_key) is not None
        else:
            raise KeyError(f"不支持的断言方式: {validate}")

