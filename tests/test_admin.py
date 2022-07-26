from page_objects.AdminPage import AdminPage

class TestAdmin:

    def test_login_username(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_user_name() == "Username"

    def test_login_username(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_user_password() == "Password"

    def test_login_forgotten_password(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_forgotten_password() == "Forgotten Password"

    def test_login_button_login(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_button_login().text == "Login"

    def test_login_button_login_enabled(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert admin_page.check_button_login().is_enabled()

    def test_login_to_admin_page(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert driver.title == "Administration"
        admin_page.login()
        assert driver.title == "Dashboard"

    def test_add_new_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} already exists"
        admin_page.add_new_product(product_name)
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"

    def test_delete_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"
        admin_page.delete_product()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} still exists"
