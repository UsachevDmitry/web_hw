from selenium.webdriver.common.by import By
from .BasePage import BasePage

class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "div#logo > a > img")
    HEADER_LINKS = (By.CSS_SELECTOR, "#top-links li")
    TAG = (By.TAG_NAME, "li")
    MENU = (By.ID, "menu")
    FOOTER = (By.CSS_SELECTOR, "footer > div > p")
    SEARCH_FIELD = (By.NAME, "search")

    CURRENCY = {
        "GBP": "£",
        "EUR": "€",
        "USD": "$"
    }
    CURRENCY_BTN = (By.CSS_SELECTOR, "#top .btn-group")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    CURRENCY_SIGN = (By.CSS_SELECTOR, "button.btn-link strong")

    def check_shop_logo(self):
        return self._verify_element_visibility(self.LOGO)

    def check_count_heading_links(self):
        return len(self._verify_elements_presence(self.HEADER_LINKS))

    def search_placeholder(self):
        search = self._verify_element_visibility(self.SEARCH_FIELD)
        return search.get_attribute("placeholder")

    def check_categories_in_menu(self):
        menu = self._verify_element_visibility(self.MENU)
        return menu.text

    def check_footer_rights(self):
        footer = self._verify_element_visibility(self.FOOTER)
        return footer.text

    def change_currency(self, value):
        self._find_element_and_click(self.CURRENCY_BTN)
        self._verify_element_visibility(self.CURRENCY_DROPDOWN)
        self._find_element_and_click((By.CSS_SELECTOR, f".currency-select[name='{value}']"))

    @property
    def current_sign_currency(self):
        return self._verify_element_visibility(self.CURRENCY_SIGN).text
