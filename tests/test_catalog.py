import allure
import pytest
from page_objects.CatalogPage import CatalogPage

@allure.title("test login button enabled")
@pytest.mark.parametrize("cat1,cat2",[('Desktops','desktops'),
                                      ('Laptops & Notebooks','laptop-notebook'),
                                      ('Software','software'),
                                      ('Phones & PDAs','smartphone'),
                                      ('Tablets','tablet'),
                                      ('Cameras', 'camera'),
                                      ('MP3 Players', 'mp3-players'),
                                      ])

@allure.title("test category name")
def test_check_category_name(driver,cat1,cat2):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page(cat2)
    assert cat1 == catalog_page.check_category_name()

@allure.title("test count cards on page")
def test_check_cards_on_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_laptop_page()
    assert catalog_page.count_product_cards == 5

@allure.title("test catalog page")
def test_catalog_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_laptop_page()
    catalog_page.sort_products_by("Price (High > Low)")
    assert catalog_page.get_current_sort_filter == "Price (High > Low)"

@allure.title("test add to cart")
def test_add_to_cart(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('tablet')
    assert catalog_page.check_add_to_cart() == "ADD TO CART"

@allure.title("test numbers of output elements")
def test_check_number_of_output_elements(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('desktops')
    assert catalog_page.check_number_of_output_elements(driver) == "15"

@allure.title("test sort elements")
def test_check_sort_elements(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('desktops')
    assert catalog_page.check_sort_elements(driver) == "Default"
