import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
PATH = "https://rahulshettyacademy.com/angularpractice/"

def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     action="store",
                     default="chrome",
                     help="Browser. Valid options are firefox, ie and chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe", options=chrome_options)
        # driver.set_window_size("1920", "1080")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="c:/webdirver/geckodriver.exe")
        # firefox option
    elif browser_name == "IE":
        pass
        # IE option

    driver.get(PATH)
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    request.cls.wait = wait
    request.cls.action = action
    request.cls.driver = driver
    yield
    driver.close()
