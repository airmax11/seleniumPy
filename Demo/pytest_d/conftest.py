import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
PATH = "https://rahulshettyacademy.com/angularpractice/"


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe", options=chrome_options)
    # driver.set_window_size("1920", "1080")
    driver.maximize_window()
    driver.get(PATH)
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    request.cls.wait = wait
    request.cls.action = action
    request.cls.driver = driver
    yield
    driver.close()




@pytest.fixture(scope="class")
def dataload():
    print("Test Case started")
    return "BLABLABLA"


@pytest.fixture(params=[("Chrome", "AirMax"), ("mozilla", "Test"), ("IE", "New")])
def sentparameters(request):
    return request.param
