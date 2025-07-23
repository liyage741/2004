# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:login_page_locators.py
# Author: liyage
# Time:2025年07月21日
import re
class LoginPageLocators:
    # 使用角色(role)和名称(name)定位元素
    USERNAME_INPUT = {"role": "textbox", "name": "请输入账号"}
    PASSWORD_INPUT = {"role": "textbox", "name": "请输入密码"}
    LOGIN_BUTTON = {"text": "登录", "exact": True}    # exact=True 表示精确匹配


class DashboardLocators:
    API_GATEWAY_ITEM = {"base": "div", "text": re.compile(r"^API网关$"), "child": "span"}
    API_GATEWAY_XPATH = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[6]/span'
