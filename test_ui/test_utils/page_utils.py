# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:page_utils.py
# Author: liyage
# Time:2025年07月22日
from time import sleep
from playwright.sync_api import Page, expect
import allure
from Common.logger import logger

class PageUtils:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("添加页面截图")
    def take_screenshot(self, name: str):
        """添加截图到Allure报告"""
        sleep(1)
        self.page.wait_for_load_state("networkidle")
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name, allure.attachment_type.PNG)
        logger.info("%s：添加截图到Allure报告" % name)

    @allure.step("获取元素文本内容")
    def result(self, element: str) -> str:
        """获取页面元素的文本内容"""
        self.page.wait_for_selector(element, timeout=5000)
        return self.page.text_content(element) or ""

    @allure.step("验证元素可见性")
    def assert_element_visible(self, element_locator: str, placeholder_value: str = None) -> None:
        try:
            actual_locator = element_locator
            if placeholder_value is not None:
                actual_locator = element_locator.replace("qingzhou-test-service", placeholder_value)
            self.page.wait_for_selector(f":has-text('{actual_locator}')", state="visible", timeout=5000)
            expect(self.page.get_by_text(actual_locator)).to_be_visible()
            logger.info(f"验证成功: 元素 '{actual_locator}' 可见")
        except Exception as e:
            logger.error(f"验证失败: 元素 '{actual_locator}' 不可见 - {str(e)}")
            raise AssertionError(f"元素 '{actual_locator}' 未显示在页面上")