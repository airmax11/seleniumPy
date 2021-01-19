import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display


PATH = "https://rahulshettyacademy.com/angularpractice/"

driver = None


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     action="store",
                     default="chrome",
                     help="Browser. Valid options are firefox, ie and chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe", options=chrome_options)
        # driver.set_window_size("1920", "1080")
        driver.maximize_window()
    elif browser_name == "chromium":
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        driver = webdriver.Chrome('/usr/bin/chromedriver')
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            print(file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % ("../picture/" + file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("../picture/" + name)
