# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:service_page.py
# Author: liyage
# Time:2025年07月22日
from playwright.sync_api import Page
from Common.commom_data import CommonData
import allure
from Common.logger import logger
from test_ui.elements.login.login_page_locators import *
from test_ui.elements.service.service_page_locators import *
from test_ui.test_utils.page_utils import PageUtils

# 全局变量
COMMON_DATA = CommonData()


class ServicePage:
    def __init__(self, page: Page):
        self.page = page
        self.utils = PageUtils(page)
        self.elements = ServiceManagementLocators()

    @allure.step("进入服务管理页面")
    def click_serviceManagement(self):
        try:
            element_info = self.page.get_by_role(
                self.elements.SERVICE_MANAGEMENT_ITEM["role"],
                name=self.elements.SERVICE_MANAGEMENT_ITEM["name"])
            element_info.click()
            logger.info("点击服务管理菜单, 操作元素: role=%s, name=%s",
                        self.elements.SERVICE_MANAGEMENT_ITEM["role"], self.elements.SERVICE_MANAGEMENT_ITEM["name"])
        except Exception as e:
            logger.error("点击服务管理菜单失败, 操作元素: role=%s, name=%s, 错误: %s",
                         self.elements.SERVICE_MANAGEMENT_ITEM["role"], self.elements.SERVICE_MANAGEMENT_ITEM["name"],
                         str(e))
            raise Exception(f"点击服务管理菜单失败: {str(e)}")

    @allure.step("点击创建服务")
    def click_createService(self):
        try:
            element_info = self.page.locator(self.elements.CREATE_SERVICE_BTN["base"]).filter(
                has_text=self.elements.CREATE_SERVICE_BTN["text"])
            element_info.click()
            logger.info("点击'创建服务'按钮, 操作元素: base=%s, text=%s", self.elements.CREATE_SERVICE_BTN["base"],
                        self.elements.CREATE_SERVICE_BTN["text"])
        except Exception as e:
            logger.error("点击'创建服务'按钮失败, 操作元素: base=%s, text=%s, 错误: %s",
                         self.elements.CREATE_SERVICE_BTN["base"], self.elements.CREATE_SERVICE_BTN["text"], str(e))
            raise Exception(f"点击'创建服务'按钮失败: {str(e)}")

    @allure.step("协议类型")
    def select_protocol(self, protocol_name: str):
        try:
            locator = self.elements.protocol_locator(protocol_name)
            element_info = self.page.get_by_role(locator["role"], name=locator["name"], exact=locator["exact"])
            element_info.click()
            logger.info("选择协议: '%s', 操作元素: role=%s, name=%s, exact=%s", protocol_name, locator["role"],
                        locator["name"], locator["exact"])
        except Exception as e:
            logger.error("选择协议失败: '%s', 操作元素: role=%s, name=%s, exact=%s, 错误: %s", protocol_name,
                         locator["role"], locator["name"], locator["exact"], str(e))
            raise Exception(f"选择协议'{protocol_name}'失败: {str(e)}")

    @allure.step("输入服务名称")
    def input_serviceName(self, service_name: str):
        try:
            placeholder_text = self.elements.SERVICE_NAME_INPUT["placeholder"]
            element = self.page.get_by_placeholder(placeholder_text)
            element.fill(service_name)
            logger.info("输入服务名称: %s, 操作元素: placeholder=%s",
                        service_name, placeholder_text)
        except Exception as e:
            logger.error("输入服务名称失败: %s, 操作元素: placeholder=%s, 错误: %s",
                         service_name, placeholder_text, str(e))
            raise Exception(f"输入服务名称失败: {service_name}, 错误: {str(e)}")

    @allure.step("输入服务别名")
    def input_serviceAlias(self, service_alias: str):
        try:
            placeholder_text = self.elements.SERVICE_DESC_INPUT["placeholder"]
            element = self.page.get_by_placeholder(placeholder_text)
            element.fill(service_alias)
            logger.info("输入服务别名: %s, 操作元素: placeholder=%s",
                        service_alias, placeholder_text)
        except Exception as e:
            logger.error("输入服务别名失败: %s, 操作元素: placeholder=%s, 错误: %s",
                         service_alias, placeholder_text, str(e))
            raise Exception(f"输入服务别名失败: {service_alias}, 错误: {str(e)}")

    @allure.step("选择网关")
    def select_gateway(self, gateway_name: str):
        try:
            placeholder_text = self.elements.GATEWAY_SELECTOR["placeholder"]
            dropdown = self.page.get_by_placeholder(placeholder_text)
            dropdown.click()
            locator = self.elements.gateway_locator(gateway_name)
            option = self.page.get_by_text(locator["text"], exact=locator["exact"])
            option.click()
            logger.info("选择网关: %s, 操作元素: placeholder=%s, 选项文本=%s",
                        gateway_name, placeholder_text, locator["text"])
        except Exception as e:
            logger.error("选择网关失败: %s, 操作元素: placeholder=%s, 选项文本=%s, 错误: %s",
                         gateway_name, placeholder_text, locator["text"], str(e))
            raise Exception(f"选择网关失败: {gateway_name}, 错误: {str(e)}")

    @allure.step("选择注册中心和应用")
    def select_registry_and_application(self, registry_type_name: str, application_name: str):
        try:
            placeholder_registry = self.elements.REGISTRY_TYPE_SELECTOR["placeholder"]
            dropdown_registry = self.page.get_by_placeholder(placeholder_registry)
            dropdown_registry.click()
            registry_locator = self.elements.register_locator(registry_type_name)
            registry_option = self.page.get_by_text(registry_locator["text"], exact=registry_locator["exact"])
            registry_option.click()
            logger.info("选择注册中心类型: %s, 操作元素: placeholder=%s, 选项文本=%s",
                        registry_type_name, placeholder_registry, registry_locator["text"])
            placeholder_app = self.elements.APP_NAME_SELECTOR["placeholder"]
            dropdown_app = self.page.get_by_placeholder(placeholder_app)
            dropdown_app.click()
            app_locator = self.elements.application_locator(application_name)
            app_option = self.page.get_by_text(app_locator["text"], exact=app_locator["exact"])
            app_option.click()
            logger.info("选择应用名称: %s, 操作元素: placeholder=%s, 选项文本=%s",
                        application_name, placeholder_app, app_locator["text"])
        except Exception as e:
            logger.error("选择注册中心或应用失败: 注册中心=%s, 应用=%s, 错误: %s",
                         registry_type_name, application_name, str(e))
            raise Exception(
                f"选择注册中心或应用失败: 注册中心={registry_type_name}, 应用={application_name}, 错误={str(e)}")

    @allure.step("选择域名")
    def select_domain(self, domain: str):
        try:
            locator = self.elements.domain_locator(domain)
            domain_element = self.page.get_by_text(locator["text"], exact=False).first
            domain_element.click()
            logger.info("选择域名: %s, 操作元素: base=%s, text=%s, child=%s",
                        domain, locator["base"], locator["text"], locator["child"])
        except Exception as e:
            logger.error("选择域名失败: %s, 操作元素: base=%s, text=%s, child=%s, 错误: %s",
                         domain, locator["base"], locator["text"], locator["child"], str(e))
            raise Exception(f"选择域名失败: {domain}, 错误: {str(e)}")

    @allure.step("点击确定按钮")
    def click_confirm(self):
        try:
            locator = self.elements.CONFIRM_BUTTON
            text_pattern = locator["text"]
            element = self.page.get_by_text(text_pattern, exact=True)
            element.click()
            logger.info("点击确定按钮, 操作元素: base=%s, text=%s", locator["base"], text_pattern.pattern)
            self.utils.take_screenshot("点击确认按钮后截图")
        except Exception as e:
            logger.error("点击确定按钮失败, 操作元素: base=%s, text=%s, 错误: %s",
                         locator["base"], text_pattern.pattern, str(e))
            raise Exception(f"点击确定按钮失败: {str(e)}")

    @allure.step("查询服务")
    def search_service(self, gateway_name: str, service_name: str):
        try:
            gateway_selector = self.elements.GATEWAY_SELECTOR["placeholder"]
            self.page.get_by_placeholder(gateway_selector).click()
            self.page.locator("form").get_by_text(gateway_name, exact=True).click()
            service_placeholder = self.elements.SERVICE_SEARCH["placeholder"]
            self.page.get_by_placeholder(service_placeholder).fill(service_name)
            self.page.locator(self.elements.FORM_LINK["base"]).click()
            logger.info(f"查询服务: 网关={gateway_name}, 服务={service_name}")
        except Exception as e:
            logger.error("搜索服务失败: 网关=%s, 服务=%s, 错误: %s", gateway_name, service_name, str(e))
            raise Exception(f"搜索服务失败: 网关={gateway_name}, 服务={service_name}, 错误={str(e)}")

    @allure.step("删除服务")
    def delete_service(self):
        try:
            delete_locator = self.elements.DELETE_BUTTON
            self.page.get_by_text(delete_locator["text"], exact=True).click()
            confirm_locator = self.elements.CONFIRM_BUTTON
            self.page.get_by_text(confirm_locator["text"], exact=True).click()
            logger.info("删除服务: text=%s", delete_locator["text"])
        except Exception as e:
            logger.error("删除服务并确认操作失败: 错误=%s", str(e))
            raise Exception(f"删除服务并确认操作失败: {str(e)}")