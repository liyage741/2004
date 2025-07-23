import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_type():
    with sync_playwright() as p:
        yield p.chromium

@pytest.fixture(scope="function", autouse=True)
def browser(browser_type):
    browser = browser_type.launch(headless=False,
                                  args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page(no_viewport=True)
    page.goto("about:blank")
    page.evaluate("() => window.moveTo(0, 0)")
    page.evaluate("() => window.resizeTo(screen.width, screen.height)")
    yield page
    page.close()