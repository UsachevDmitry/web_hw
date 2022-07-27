import allure
from page_objects.AdminPage import AdminPage

@allure.feature('Admin')
class TestAdmin:

    @allure.title("test login username")
    def test_login_username(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_user_name() == "Username"

    @allure.title("test login password")
    def test_login_password(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_user_password() == "Password"

    @allure.title("test forgotten password")
    def test_login_forgotten_password(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_forgotten_password() == "Forgotten Password"

    @allure.title("test login button login")
    def test_login_button_login(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_button_login().text == "Login"

    @allure.title("test login button enabled")
    def test_login_button_login_enabled(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_button_login().is_enabled()

    @allure.title("test authorization to admin")
    def test_login_to_admin_page(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert driver.title == "Administration"
        admin_page.login()
        assert driver.title == "Dashboard"

    @allure.title("test add product in admin")
    def test_add_new_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} already exists"
        admin_page.add_new_product(product_name)
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"

    @allure.title("test delete product in admin")
    def test_delete_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"
        admin_page.delete_product()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} still exists"
