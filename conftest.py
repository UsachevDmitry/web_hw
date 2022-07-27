import os
import pytest
import allure
import datetime
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.opera import OperaDriverManager
from utils import setup_logging

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'driver' in item.fixturenames:
                web_driver = item.funcargs['driver']
            else:
                print('Fail to take screen-shot')
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        print('Fail to take screen-shot: {}'.format(e))

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/otus/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.1.41:8081/")
    parser.addoption("--executor", action="store", default="192.168.1.41")
    parser.addoption("--logs", default=True)
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--videos", default=False)
    parser.addoption("--vnc", default=True)

def driver_factory(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == "local":
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

    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser_name,
            "name": "Tester",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }
        browser = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    return browser

@pytest.fixture
def driver(request):
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    test_name = request.node.name

    logger = setup_logging(log_level, test_name)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    browser = driver_factory(request)
    browser.maximize_window()
    browser.test_name = test_name
    browser.log_level = log_level
    browser.url = url
    browser.logger = logger
    logger.info("Browser: {}".format(browser.capabilities))

    def fin():
        browser.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))
    request.addfinalizer(fin)
    return browser
