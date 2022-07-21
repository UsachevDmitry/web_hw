import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("cat1,cat2",[('Desktops','desktops'),
                                      ('Laptops & Notebooks','laptop-notebook'),
                                      ('Software','software'),
                                      ('Phones & PDAs','smartphone'),
                                      ('Tablets','tablet'),
                                      ('Cameras', 'camera'),
                                      ('MP3 Players', 'mp3-players'),
                                      ])
def test_check_category_name(driver,url,cat1,cat2):
    driver.get(url + cat2)
    category_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2")))
    assert cat1 == category_name.text


def test_check_cards_on_page(driver,url):
    driver.get(url + 'laptop-notebook')
    content = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content")))
    elements = content.find_elements(By.CLASS_NAME, 'product-layout')
    assert len(elements) == 5

def test_add_to_cart(driver,url):
    driver.get(url + 'tablet')
    cart = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-group")))
    assert cart.find_element(By.TAG_NAME, "span").text == "ADD TO CART"

def test_check_number_of_output_elements(driver,url):
    driver.get(url + 'desktops')
    sort_filter = driver.find_element(By.CSS_SELECTOR, "#input-limit > option[selected]")
    assert "20" == sort_filter.text

def test_check_sort_elements(driver,url):
    driver.get(url + 'desktops')
    sort_filter = driver.find_element(By.CSS_SELECTOR, "#input-sort > option[selected]")
    assert "Default" == sort_filter.text
