import pytest
from selenium import webdriver

from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    # -----1.Launch google Chrome-----
    # initialize webdriver
    browser = ReadConfiguration.read_configuration("Basic info", "browser")
    driver = None
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.edge()
    else:
        print("provide valid browser name")

    # -----2.open website-----
    # open URL and Maximize window
    driver.maximize_window()
    app_url = ReadConfiguration.read_configuration("Basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield
    # quit
    driver.quit()