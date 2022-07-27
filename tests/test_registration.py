import allure
from page_objects.RegisterPage import RegisterPage

@allure.title("test register acc")
def test_register_acc(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    assert register_page.check_register_acc() == "Register Account"

@allure.title("test registr")
def test_register(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    assert "Register" in register_page.check_list()

@allure.title("test my account")
def test_my_account(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    assert "My Account" in register_page.check_list()

@allure.title("test password include")
def test_password_inc(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    for i in register_page.check_password_inc():
        assert i.get_attribute("type") == "password"

@allure.title("test continue button")
def test_continue_button(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    assert register_page.check_continue_button().is_enabled()

@allure.title("test user registration")
def test_user_registration(driver):
    register_page = RegisterPage(driver)
    register_page.open_registr_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
