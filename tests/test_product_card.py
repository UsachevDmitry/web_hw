from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_card_apple(driver,url):
    driver.get(url + 'component/monitor/test')
    element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 > h1")))
    assert element.text == 'Apple Cinema 30"'

def test_product_card_price(driver, url):
    driver.get(url + 'component/monitor/test')
    element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")))
    assert element.text == '$110.00'

def test_product_card_button(driver, url):
    driver.get(url + 'component/monitor/test')
    button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    assert button.is_enabled()

def test_product_card_button_uf(driver, url):
    driver.get(url + 'component/monitor/test')
    uf = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "button-upload222")))
    assert uf.text == "Upload File"

def test_available_options(driver, url):
    driver.get(url + 'component/monitor/test')
    ao = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "product")))
    assert ao.find_element(By.TAG_NAME, "h3").text == "Available Options"

