from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_acc(driver, url):
    driver.get(url + 'index.php?route=account/register')
    page_title = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > h1")))
    assert page_title.text == "Register Account"

def test_register(driver, url):
    driver.get(url + 'index.php?route=account/register')
    account_links = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-group")))
    assert "Register" in account_links.text

def test_my_account(driver, url):
    driver.get(url + 'index.php?route=account/register')
    account_links = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-group")))
    assert "My Account" in account_links.text

def test_password_inc(driver, url):
    driver.get(url + 'index.php?route=account/register')
    password_fieldset = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "fieldset:nth-child(2)")))
    password_fields = password_fieldset.find_elements(By.CSS_SELECTOR, "input")
    for i in password_fields:
        assert i.get_attribute("type") == "password"

def test_continue_button(driver, url):
    driver.get(url + 'index.php?route=account/register')
    continue_button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='submit']")))
    assert continue_button.is_enabled()