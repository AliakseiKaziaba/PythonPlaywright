import pytest
from playwright.sync_api import Page

from OnlinerProject.pages.OnlinerPageHelper import OnlinerPageHelper
from OnlinerProject.tests.conftest import chromium_page


@pytest.fixture
def onliner_page(chromium_page: Page) -> OnlinerPageHelper:
    return OnlinerPageHelper(page=chromium_page)
