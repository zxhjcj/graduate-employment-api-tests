def get_value(res, check_key):
    if check_key == "status_code":
        return res.status_code

    if check_key.startswith("body."):
        try:
            value = res.json()
        except ValueError as e:
            raise AssertionError(f"响应不是合法 JSON，无法读取 {check_key}: {res.text}") from e
        for key in check_key.split(".")[1:]:
            if isinstance(value, list):
                key = int(key)
            value = value[key]
        return value

    raise KeyError(f"不支持的校验字段: {check_key}")


def assert_validate(res, validate_data):
    for validate in validate_data or []:
        if "eq" in validate:
            check_key, expected = validate["eq"]
            assert get_value(res, check_key) == expected
        elif "contains" in validate:
            check_key, expected = validate["contains"]
            assert expected in get_value(res, check_key)
        elif "len_eq" in validate:
            check_key, expected = validate["len_eq"]
            assert len(get_value(res, check_key)) == expected
        elif "status_in" in validate:
            expected = validate["status_in"]
            assert res.status_code in expected
        elif "not_null" in validate:
            check_key = validate["not_null"][0]
            assert get_value(res, check_key) is not None
        else:
            raise KeyError(f"不支持的断言方式: {validate}")
