from OnlinerProject.pages.BasePage import BasePage


class OnlinerPageHelper(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.locator_smartphone_link = self.locator(
            xpath="//a[contains(@href,'mobile') and contains(@class,'project-navigation__link_primary')]")
        self.locator_mobile_phones_title = self.locator(css="h1:has-text('Мобильные телефоны')")

    def click_smartphone_link(self):
        self.locator_smartphone_link.click()

    def check_mobile_phones_title(self):
        self.expect_visible(self.locator_mobile_phones_title)