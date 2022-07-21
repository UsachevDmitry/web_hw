import os
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.opera import OperaDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/otus/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.1.41:8081/")

@pytest.fixture
def url(request):
    url_option = request.config.getoption("--url")
    yield url_option

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        browser = webdriver.Chrome(executable_path=f"{drivers}/chromedriver", options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        browser = webdriver.Firefox(executable_path=f"{drivers}/geckodriver", options=options)
    elif browser_name == "opera":
        options = ChromeOptions()
        if headless:
            options.headless = True
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise ValueError("Browser not supported!")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser