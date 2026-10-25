# 毕业生就业系统接口自动化测试

基于 **Python + pytest + Requests + YAML + Allure** 的接口自动化学习项目，覆盖登录、毕业生档案查询与修改流程。仓库只包含测试代码，不包含被测系统后端。

## 已实现功能

- YAML 管理请求数据和预期结果，使用 pytest 参数化执行。
- 封装请求发送、环境配置读取与响应断言。
- 支持状态码、相等、包含、长度和非 NULL 等校验。
- 登录用例提取 token，保存到本地 `extract.yaml`；后续请求使用 `${token}` 引用。
- session fixture 在执行前初始化提取文件，标记与排序逻辑确保登录先执行。
- 支持 `TEST_ENV`、`BASE_URL` 环境变量覆盖配置，生成 Allure 原始结果和报告。
- `api_practice/` 保留参数化、fixture 等独立练习，不是默认执行入口。

## 目录

```text
common/                 请求、配置、断言、日志与 YAML 工具
testcase/               主测试用例及 YAML 数据
api_practice/           独立学习练习
config.yaml             本地环境地址与超时配置
extract.example.yaml    运行时变量文件示例
pytest.ini              收集规则及 Allure 参数
requirements.txt        Python 依赖
run.py                  执行测试并生成报告的入口
```

## 安装

建议 Python 3.10 及以上。在项目根目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 准备被测服务

需自行启动与用例匹配的毕业生就业系统，并准备专用测试账号和数据。默认地址为 `http://localhost:8080`，涉及接口：

- `POST /api/auth/login`
- `GET /api/graduate/profile`
- `PUT /api/graduate/profile`

用例中的 `stu001`、密码及档案内容是本地演示测试数据，运行前应改为自己的专用测试数据，不要填写真实用户信息或生产凭据。修改接口会改变测试账号档案，请仅在允许修改的测试环境执行。

可修改 `config.yaml`，也可在 PowerShell 中设置：

```powershell
$env:TEST_ENV = "test"
$env:BASE_URL = "http://localhost:8080"
```

## 运行

```powershell
# 仅检查用例收集，不向被测服务发起请求
.\.venv\Scripts\python.exe -m pytest --collect-only -o addopts=""

# 执行默认主测试集，生成 Allure 原始结果到 temps/
.\.venv\Scripts\python.exe -m pytest
```

报告生成需要另行安装 Allure 命令行工具及其所需 Java 环境，并确保 `allure` 位于 PATH：

```powershell
allure generate ./temps -o ./report --clean
allure open ./report
```

安装好 Allure CLI 后，也可以执行 `python run.py`。当前入口不会根据 pytest 返回码阻止后续报告生成，查看运行结果时应同时关注控制台和报告。

## 当前限制

- 主测试集是串行、有关联的业务流程，查询与修改依赖登录产生的 token，不适合直接并行执行。
- `not_null` 只校验非 NULL，不代表字符串或集合非空。
- 当前日志可能记录完整响应和 token，日志及原始报告仅在本地保留；后续可完善脱敏。
- `api_practice/` 部分练习脚本可能在导入时访问本地服务，不应直接扩大默认收集范围。
- 完整接口执行依赖本地服务与测试数据；用例收集成功不代表接口测试通过。

## 发布范围

运行时 token、日志、报告、虚拟环境、IDE 配置、简历和临时文件均通过 `.gitignore` 排除，不随源码上传。
