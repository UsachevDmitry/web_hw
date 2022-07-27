import allure
import pytest
from page_objects.MainPage import MainPage

@allure.title("test check logo title")
def test_check_logo_title(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    assert main_page.check_shop_logo().get_attribute("title") == 'Your Store'

@allure.title("test count of top links")
def test_count_of_top_links(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    assert main_page.check_count_heading_links() == 7

@allure.title("test search field is empty")
def test_check_search_field_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    assert main_page.search_placeholder() == "Search"

@allure.title("test categories in menu")
@pytest.mark.parametrize('category',['Desktops','Laptops & Notebooks','Components','Tablets',
                                     'Software','Phones & PDAs','Cameras','MP3 Players'])
def test_check_categories_in_menu(driver,category):
    main_page = MainPage(driver)
    main_page.open_page()
    assert category in main_page.check_categories_in_menu()

@allure.title("test footer rights")
def test_footer_rights(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    assert "Powered By OpenCart\nYour Store © 2022" in main_page.check_footer_rights()

@allure.title("test switch currency")
def test_switch_currency(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.change_currency("EUR")
    assert main_page.CURRENCY["EUR"] == main_page.current_sign_currency

@allure.title("test change currency")
def test_change_currency(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.change_currency("EUR")
    assert main_page.CURRENCY["EUR"] == main_page.current_sign_currency
