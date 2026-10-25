import pytest

from common.yaml_util import clear_yaml


@pytest.fixture(scope="module", autouse=False)
def run_around_tests():
    print("测试用例")
    yield
    print("测试用例执行完毕")

@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    clear_yaml()


def pytest_collection_modifyitems(items):
    items.sort(
        key=lambda item: item.get_closest_marker("order").args[0]
        if item.get_closest_marker("order")
        else 999
    )
