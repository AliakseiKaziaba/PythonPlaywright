from OnlinerProject.pages.BasePage import BasePage


class OnlinerPageHelper(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.smartphone_link = "//a[contains(@href,'mobile') and contains(@class,'project-navigation__link_primary')]"
        self.mobile_phones_title = "h1:has-text('{title_text}')"

    def click_smartphone_link(self):
        self.locator(xpath=self.smartphone_link).click()

    def check_mobile_phones_title(self, title_text):
        locator = self.locator(css=self.mobile_phones_title, title_text=title_text)
        self.expect_visible(locator)