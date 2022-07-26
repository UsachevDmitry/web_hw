from page_objects.ProductPage import ProductPage

def test_product_card_apple(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_apple() == 'Apple Cinema 30"'

def test_product_card_price(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_price() == '$110.00'

def test_product_card_button(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_button().is_enabled()

def test_product_card_button_uf(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_product_card_button_uf() == "Upload File"

def test_available_options(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert product_page.check_available_options() == "Available Options"
