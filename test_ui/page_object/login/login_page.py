# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:login_page.py
# Author: liyage
# Time:2025年07月21日
from time import sleep
from playwright.sync_api import Page
from Common.commom_data import CommonData
import allure

from Common.logger import logger
from test_ui.elements.login.login_page_locators import *
from test_ui.test_utils.page_utils import PageUtils

# 全局变量
COMMON_DATA = CommonData()


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = LoginPageLocators()
        self.utils = PageUtils(page)

    @allure.step("导航至轻舟平台")
    def navigate(self, url):
        try:
            self.page.goto(url, wait_until="domcontentloaded")
            logger.info("加载动态数据,打开网页：%s" % url)
        except Exception:
            raise Exception("打开%s超时请检查网络或网址服务器" % url)

    @allure.step("输入用户名")
    def fill_username(self, username: str):
        try:
            element_info = self.page.get_by_role(
                self.elements.USERNAME_INPUT["role"],
                name=self.elements.USERNAME_INPUT["name"])
            element_info.fill(username)
            logger.info("输入用户名: '%s', 操作元素: role=%s, name=%s", username,
                        self.elements.USERNAME_INPUT["role"], self.elements.USERNAME_INPUT["name"])
        except Exception as e:
            logger.error("用户名输入失败: '%s', 操作元素: role=%s, name=%s, 错误: %s", username,
                         self.elements.USERNAME_INPUT["role"], self.elements.USERNAME_INPUT["name"], str(e))
            raise Exception(f"输入用户名'{username}'失败: {str(e)}")

    @allure.step("输入密码")
    def fill_password(self, password: str):
        try:
            password_field = self.page.get_by_role(
                self.elements.PASSWORD_INPUT["role"],
                name=self.elements.PASSWORD_INPUT["name"])
            password_field.fill(password)
            logger.info("输入用户密码: '%s', 操作元素: role=%s, name=%s", password,
                        self.elements.PASSWORD_INPUT["role"], self.elements.PASSWORD_INPUT["name"])
        except Exception as e:
            logger.error("用户密码输入失败: '%s', 操作元素: role=%s, name=%s, 错误: %s", password,
                         self.elements.PASSWORD_INPUT["role"], self.elements.PASSWORD_INPUT["name"], str(e))
            raise Exception(f"输入用户密码'{password}'失败: {str(e)}")

    @allure.step("登录轻舟平台")
    def click_login(self):
        try:
            element_info = self.page.get_by_text(
                self.elements.LOGIN_BUTTON["text"],
                exact=self.elements.LOGIN_BUTTON["exact"])
            element_info.click()
            logger.info("点击登录按钮, 操作元素: text='%s', exact=%s", self.elements.LOGIN_BUTTON["text"],
                        self.elements.LOGIN_BUTTON["exact"])
        except Exception as e:
            logger.error("点击登录按钮失败, 操作元素: text='%s', exact=%s, 错误: %s",
                         self.elements.LOGIN_BUTTON["text"], self.elements.LOGIN_BUTTON["exact"], str(e))
            raise Exception(f"点击登录按钮失败: {str(e)}")

    @allure.step("登录轻舟平台")
    def login(self, url, username: str, password: str):
        self.navigate(url)
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        self.navigate_to_apigw()

    @allure.step("导航API网关")
    def navigate_to_apigw(self):
        try:
            locator_info = {"base": DashboardLocators.API_GATEWAY_ITEM["base"],
                            "text": DashboardLocators.API_GATEWAY_ITEM["text"],
                            "child": DashboardLocators.API_GATEWAY_ITEM["child"]}
            self.page.locator(locator_info["base"]).filter(has_text=locator_info["text"]).locator(
                locator_info["child"]).click()
            logger.info("导航至API网关, 操作元素: base='%s', text='%s', child='%s'", locator_info["base"],
                        locator_info["text"], locator_info["child"])
        except Exception as e:
            logger.error("导航至API网关失败, 操作元素: base='%s', text='%s', child='%s', 错误: %s",
                         locator_info["base"], locator_info["text"], locator_info["child"], str(e))
            raise Exception(f"导航至API网关失败: {str(e)}")


    # 添加截图方法
    def take_screenshot(self, name: str):
        return self.utils.take_screenshot(name)

    def result(self, element) -> str:
        return self.utils.result(element)
