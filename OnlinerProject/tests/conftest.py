import pytest
from playwright.sync_api import Playwright, Page

pytest_plugins = (
    "OnlinerProject.pages.fixtures.Pages"
)


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)

    yield browser.new_page()

    browser.close()
