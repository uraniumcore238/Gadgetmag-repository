import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("Starting with Chrome")
        driver = webdriver.Chrome(executable_path="D:\\Programming\\Gadgetmag\\Sourse\\chromedriver.exe")
    elif browser_name == "firefox":
        print("Starting with Firefox")
        driver = webdriver.Firefox(executable_path="D:\\Programming\\Gadgetmag\\Sourse\\geckodriver.exe")
    elif browser_name == "ie":
        print("Starting with IE")
        driver = webdriver.Ie(executable_path="\\Sourse\\chromedriver.exe")

    driver.get("https://neyvabank.ru/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    print("Closing driver")
    driver.close()
    driver.quit()
