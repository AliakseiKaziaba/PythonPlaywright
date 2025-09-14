from OnlinerProject.configuration import ProjectUrls
from OnlinerProject.pages.OnlinerPageHelper import OnlinerPageHelper


def test_open_onliner_smartphones_1(onliner_page: OnlinerPageHelper):
    onliner_page.go_to_site(ProjectUrls.ONLINER_URL)
    onliner_page.click_smartphone_link()
    onliner_page.check_mobile_phones_title(title_text="Мобильные телефоны")
