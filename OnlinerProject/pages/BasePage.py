from playwright.sync_api import expect


class BasePage:
    default_timeout = 5000

    def __init__(self, page):
        self.page = page

    def go_to_site(self, url):
        self.page.goto(url, wait_until='networkidle')
        # wait_until='networkidle' to wait for all network requests to be downloaded before next steps

    def refresh_page(self):
        self.page.reload(wait_until='domcontentloaded')

    def hover_on_element(self, locator):
        self.page.hover(locator)

    def locator(
            self,
            test_id: str = None,
            css: str = None,
            xpath: str = None
    ):
        if test_id:
            loc = self.page.get_by_test_id(test_id)
        elif xpath:
            loc = self.page.locator(f'xpath={xpath}')
        elif css:
            loc = self.page.locator(css)
        else:
            raise ValueError("You must specify at least one search method: test_id, css or xpath")
        return loc

    @staticmethod
    def expect_visible(element_locator, timeout=default_timeout):
        expect(element_locator).to_be_visible(timeout=timeout)

    @staticmethod
    def expect_hidden(element_locator, timeout=default_timeout):
        expect(element_locator).to_be_hidden(timeout=timeout)

    @staticmethod
    def expect_have_text(element_locator, text):
        expect(element_locator).to_have_text(text)
