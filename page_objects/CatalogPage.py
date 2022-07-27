import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .BasePage import BasePage

class CatalogPage(BasePage):
    NOTEBOOKS_BTN = (By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(2)")
    SHOW_ALL_BTN = (By.CSS_SELECTOR, "li.dropdown.open .see-all")
    CONTENT = (By.CSS_SELECTOR, "#content .product-grid")
    SORT_FILTER = (By.CSS_SELECTOR, "select#input-sort")
    DEVICES = (By.CSS_SELECTOR, "#content > h2")
    BTN_GROUP = (By.CSS_SELECTOR, ".button-group")
    SPAN = "span"
    OPTION = "#input-limit > option[selected]"
    OPTION2 ="#input-sort > option[selected]"

    def open_page(self, cat2):
        with allure.step(f"page opens {self.driver.url}"):
            self.driver.get(self.driver.url + cat2)

    def check_category_name(self):
        category_name = self._verify_element_visibility(self.DEVICES,5)
        return category_name.text

    def open_laptop_page(self):
        self.driver.get(self.driver.url)
        self._find_element_and_click(self.NOTEBOOKS_BTN)
        self._find_element_and_click(self.SHOW_ALL_BTN)

    def check_add_to_cart(self):
        cart = self._verify_element_visibility(self.BTN_GROUP)
        return cart.find_element(By.TAG_NAME, self.SPAN).text

    def check_number_of_output_elements(self,driver):
        return driver.find_element(By.CSS_SELECTOR, self.OPTION).text

    def check_sort_elements(self,driver):
        return driver.find_element(By.CSS_SELECTOR, self.OPTION2).text

    def sort_products_by(self, text="Price (High > Low)"):
        sort_filter = Select(self._verify_element_visibility(self.SORT_FILTER))
        sort_filter.select_by_visible_text(text)

    @property
    def count_product_cards(self):
        content = self._verify_elements_visibility(self.CONTENT)
        return len(content)

    @property
    def get_current_sort_filter(self):
        sort_filter = Select(self._verify_element_visibility(self.SORT_FILTER))
        return sort_filter.first_selected_option.text
