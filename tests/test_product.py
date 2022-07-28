import allure
from page_objects.ProductPage import ProductPage

@allure.title("test product card apple")
def test_product_card_apple(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_apple() == 'Apple Cinema 30"'

@allure.title("test product card price")
def test_product_card_price(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_price() == '$110.00'

@allure.title("test product card button")
def test_product_card_button(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_button().is_enabled()

@allure.title("test product card button uf")
def test_product_card_button_uf(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_button_uf() == "Upload File"

@allure.title("test available options")
def test_available_options(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_available_options() == "Available Options"
