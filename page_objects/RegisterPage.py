from selenium.webdriver.common.by import By
from .BasePage import BasePage

class RegisterPage(BasePage):
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[title='My Account']")
    REGISTER_BTN = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")
    LIST = (By.CSS_SELECTOR, ".list-group")
    CHILD = (By.CSS_SELECTOR, "fieldset:nth-child(2)")

    TEST_USER = {
        "firstname": "Dmitry",
        "lastname": "Usachev",
        "email": "usachev.dmitry@gmail.com",
        "telephone": "12345678901",
        "password": "123456",
        "confirm": "123456",
    }

    def open_page(self):
        return self.driver.get(self.driver.url + 'index.php?route=account/register')

    def check_register_acc(self):
        return self._verify_element_visibility(self.SUCCESS_MESSAGE).text

    def check_list(self):
        return self._verify_element_visibility(self.LIST).text

    def check_password_inc(self):
        password_fieldset = self._verify_element_visibility(self.CHILD)
        return password_fieldset.find_elements(By.CSS_SELECTOR, "input")

    def check_continue_button(self):
        return self._verify_element_visibility(self.CONTINUE_BTN)

    def open_registr_page(self):
        self.driver.get(self.driver.url)
        self._find_element_and_click(self.MY_ACCOUNT_BTN)
        self._find_element_and_click(self.REGISTER_BTN)

    def create_new_user(self):
        for i in self.TEST_USER.keys():
            self._fill_input_field((By.CSS_SELECTOR, f"input[name='{i}']"), self.TEST_USER[i])
        self._find_element_and_click(self.PRIVACY_CHECKBOX)
        self._find_element_and_click(self.CONTINUE_BTN)

    @property
    def success_register_message(self):
        msg = self._verify_element_visibility(self.SUCCESS_MESSAGE)
        return msg.text
