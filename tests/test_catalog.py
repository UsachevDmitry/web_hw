import pytest
from page_objects.CatalogPage import CatalogPage

@pytest.mark.parametrize("cat1,cat2",[('Desktops','desktops'),
                                      ('Laptops & Notebooks','laptop-notebook'),
                                      ('Software','software'),
                                      ('Phones & PDAs','smartphone'),
                                      ('Tablets','tablet'),
                                      ('Cameras', 'camera'),
                                      ('MP3 Players', 'mp3-players'),
                                      ])
def test_check_category_name(driver,cat1,cat2):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page(cat2)
    assert cat1 == catalog_page.check_category_name()

def test_check_cards_on_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_laptop_page()
    assert catalog_page.count_product_cards == 5

def test_catalog_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_laptop_page()
    catalog_page.sort_products_by("Price (High > Low)")
    assert catalog_page.get_current_sort_filter == "Price (High > Low)"

def test_add_to_cart(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('tablet')
    assert catalog_page.check_add_to_cart() == "ADD TO CART"

def test_check_number_of_output_elements(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('desktops')
    assert catalog_page.check_number_of_output_elements(driver) == "15"

def test_check_sort_elements(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page('desktops')
    assert catalog_page.check_sort_elements(driver) == "Default"
