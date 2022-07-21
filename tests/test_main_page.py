import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_logo_title(driver, url):
    driver.get(url)
    logo = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#logo > a > img")))
    assert logo.get_attribute("title") == 'Your Store'

def test_count_of_top_link(driver,url):
    driver.get(url)
    header_links = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "top-links")))
    elements = header_links.find_elements(By.TAG_NAME, 'li')
    assert len(elements) == 7

def test_check_search_field_is_empty(driver,url):
    driver.get(url)
    search = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "search")))
    assert search.get_attribute("placeholder") == "Search"

@pytest.mark.parametrize('category',['Desktops','Laptops & Notebooks','Components','Tablets',
                                     'Software','Phones & PDAs','Cameras','MP3 Players'])
def test_check_categories_in_menu(driver,url,category):
    driver.get(url)
    menu = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "menu")))
    assert category in menu.text

def test_footer_rights(driver,url):
    driver.get(url)
    footer_rights= WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer > div > p")))
    assert "Powered By OpenCart\nYour Store © 2022" in footer_rights.text
