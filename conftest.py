import pytest
from playwright.sync_api import sync_playwright
from pages.password_settings_page import PasswordSettingsPage
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def password_settings_page(page):
    page_obj = PasswordSettingsPage(page)
    page_obj.open()
    return page_obj


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login