from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_username(driver,url):
    driver.get(url + 'admin')
    username_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert username_field.get_attribute("placeholder") == "Username"

def test_login_password(driver, url):
    driver.get(url + 'admin')
    username_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert username_field.get_attribute("placeholder") == "Password"

def test_login_forgotten_password(driver, url):
    driver.get(url + 'admin')
    forgotten_pswrd = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Forgotten Password")))
    assert forgotten_pswrd.text == "Forgotten Password"

def test_login_button_login(driver, url):
    driver.get(url + 'admin')
    login_btn = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert login_btn.text == "Login"

def test_login_button_login_enabled(driver, url):
    driver.get(url + 'admin')
    login_btn = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert login_btn.is_enabled()