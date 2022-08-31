import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage

class ProductPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content .col-sm-4 > h1")
    PRICE = (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")
    BTN_CART = (By.CSS_SELECTOR, "#button-cart")
    BTN_UF = (By.ID, "button-upload222")
    PRODUCT = (By.ID, "product")

    def open_page(self):
        with allure.step(f"page opens {self.driver.url}"):
            return self.driver.get(self.driver.url + 'component/monitor/test')

    def check_product_card_apple(self):
        return self._verify_element_visibility(self.CONTENT).text

    def check_product_card_price(self):
        return self._verify_element_visibility(self.PRICE).text

    def check_product_card_button(self):
        return self._verify_element_visibility(self.BTN_CART)

    def check_product_card_button_uf(self):
        return self._verify_element_visibility(self.BTN_UF).text

    def check_available_options(self):
        ao = self._verify_element_visibility(self.PRODUCT)
        return ao.find_element(By.TAG_NAME, "h3").text
