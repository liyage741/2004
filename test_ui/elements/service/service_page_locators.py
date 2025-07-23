# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:service_page_locators.py
# Author: liyage
# Time:2025年07月22日
import re
from typing import Dict, Any


class ServiceManagementLocators:
    SERVICE_MANAGEMENT_ITEM = {"role": "menuitem", "name": "服务管理"}
    CREATE_SERVICE_BTN = {"base": "a", "text": "创建服务"}
    SERVICE_NAME_INPUT = {"placeholder": "以小写字母或数字开头和结尾，支持符号：-，2-63个字符以内"}
    HTTP_RADIO = {"role": "radio", "name": "HTTP", "exact": True}
    SERVICE_DESC_INPUT = {"placeholder": "100个字符以内"}
    GATEWAY_SELECTOR = {"placeholder": "请选择网关"}
    GATEWAY_OPTION = {"text": "gateway-proxy", "exact": True}
    REGISTRY_TYPE_SELECTOR = {"placeholder": "请选择注册中心类型"}
    KUBERNETES_OPTION = {"text": "Kubernetes"}
    APP_NAME_SELECTOR = {"placeholder": "请选择应用名称"}
    APP_OPTION = {"text": "apigw-demo-e2e.apigw-demo.svc"}
    DOMAIN_INPUT = {"base": "div", "text": re.compile(r"^$"), "child": "textbox"}
    DOMAIN_OPTION = {"text": "10.104.183.13"}
    CONFIRM_BUTTON = {"base": "a", "text": re.compile(r"^确定$")}
    SERVICE_SEARCH = {"placeholder": "请输入服务名称或别名"}
    FORM_LINK = {"base": "form a"}
    DELETE_BUTTON = {"base": "a", "text": "删除"}

    @staticmethod
    def protocol_locator(protocol_name: str) -> dict:       #协议
        return {
            "role": "radio",
            "name": protocol_name,
            "exact": True
        }

    @staticmethod
    def gateway_locator(gateway_name: str) -> dict:         #网关
        return {
            "text": gateway_name,
            "exact": True
        }

    @staticmethod
    def register_locator(option_name: str) -> dict:         #注册中心
        return {
            "text": option_name,
            "exact": True
        }

    @staticmethod
    def application_locator(app_name: str) -> dict:         #应用
        return {
            "text": app_name,
            "exact": True
        }

    @staticmethod
    def domain_locator(domain: str):                        #域名
        return {
            "base": "div",
            "text": re.compile(rf"^域名{re.escape(domain)}"),
            "child": "textbox"
        }
