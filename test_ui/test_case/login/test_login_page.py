# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:test_login_page.py
# Author: liyage
# Time:2025年07月21日
import allure
import pytest
from playwright.async_api import expect
from Common.commom_data import CommonData
from Common.read_file import load_yaml
from test_ui.elements.login.login_page_locators import *
from test_ui.page_object.login.login_page import LoginPage

# 全局变量
COMMON_DATA = CommonData()


@allure.epic("轻舟登录")
@pytest.mark.smoke
class TestLogin:
    allure.dynamic.title(f"导航API网关")

    def test_login(self, page):
        login_page = LoginPage(page)
        # 登录轻舟
        login_page.navigate(COMMON_DATA.console_url)
        login_page.fill_username(COMMON_DATA.qingzhou_default_user)
        login_page.fill_password(COMMON_DATA.qingzhou_default_password)
        login_page.click_login()

        # 添加Allure报告附件
        login_page.take_screenshot("登录轻舟")
        html_content = login_page.result(DashboardLocators.API_GATEWAY_XPATH)
        assert "API网关" in html_content

        # 导航API网关
        login_page.navigate_to_apigw()

        # 添加Allure报告附件
        login_page.take_screenshot("登录网关平台")
