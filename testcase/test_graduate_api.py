import pytest
import allure

from common.assert_util import assert_validate
from common.logger_util import get_logger
from common.request_util import TestAPI
from common.yaml_util import read_yaml, read_textCase, write_yaml

logger = get_logger("testcase")


@allure.epic("毕业生就业系统")
@allure.feature("用户管理模块1")
class TestLogin:

    @allure.story("登陆接口")
    @pytest.mark.order(1)
    @pytest.mark.parametrize("case_data", read_textCase("./testcase/test_login.yaml"))
    def test_login(self, case_data):
        allure.dynamic.title(case_data["name"])
        res = TestAPI.send_case_request(case_data)
        assert_validate(res, case_data.get("validate"))

        result = res.json()
        write_yaml({"token": result["data"]["token"]})

        yaml_data = read_yaml()
        logger.info("登录接口返回: %s", result)
        logger.info("已提取 token: %s", yaml_data["token"])

    @allure.story("查询接口")
    @pytest.mark.order(2)
    @pytest.mark.parametrize("case_data", read_textCase("./testcase/test_get_graduate_profile.yaml"))
    def test_get_graduate_profile(self, case_data):
        allure.dynamic.title(case_data["name"])
        res = TestAPI.send_case_request(case_data)

        assert_validate(res, case_data.get("validate"))
        logger.info("毕业生档案查询用例断言全部通过")

    @allure.story("修改接口")
    @pytest.mark.order(3)
    @pytest.mark.parametrize("case_data", read_textCase("./testcase/test_select_update.yaml"))
    def test_select_update(self, case_data):
        allure.dynamic.title(case_data["name"])
        res = TestAPI.send_case_request(case_data)
        assert_validate(res, case_data.get("validate"))
        logger.info("毕业生修改用例断言全部通过")
