import allure
import pytest
from playwright.async_api import expect
from Common.commom_data import CommonData
from Common.read_file import load_yaml
from test_ui.elements.login.login_page_locators import *
from test_ui.page_object.login.login_page import LoginPage
from test_ui.page_object.service.service_page import ServicePage
from test_ui.test_data.gw_enum import ProtocolType, RegisterType
from test_ui.test_utils.page_utils import PageUtils

# 全局变量
COMMON_DATA = CommonData()


@allure.epic("服务管理")
@pytest.mark.smoke
class TestService:
    serviceName = "qingzhou-test-service"
    serviceAlias = "qingzhou_test_service"

    @pytest.fixture
    def login(self, page):
        login_page = LoginPage(page)
        login_page.login(COMMON_DATA.console_url, COMMON_DATA.qingzhou_default_user,
                         COMMON_DATA.qingzhou_default_password)
        yield

    def test_createService(self, page, login):
        service_page = ServicePage(page)
        page_utils = PageUtils(page)
        service_page.click_serviceManagement()
        service_page.click_createService()
        service_page.select_protocol(ProtocolType.HTTP.value)
        service_page.input_serviceName(self.serviceName)
        service_page.input_serviceAlias(self.serviceAlias)
        service_page.select_gateway(COMMON_DATA.default_gateway_name)
        service_page.select_registry_and_application(RegisterType.Kubernetes.value, COMMON_DATA.appName)
        service_page.select_domain(COMMON_DATA.hostHeader)
        service_page.click_confirm()
        service_page.search_service(COMMON_DATA.default_gateway_name, self.serviceName)
        # 断言服务创建成功
        page_utils.assert_element_visible(self.serviceName)
        service_page.delete_service()
