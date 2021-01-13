import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
# from Demo.imp import prec as dr
from Demo.utilities.BaseClass import Baseclass
from Demo.pageobject.HomePage import HomePageObject



class Testsuit_01(Baseclass):

    def test_e2e(self):
        homepage = HomePageObject(self.driver)
        homepage.shop_button_click()
        prod = "//div[@class='card h-100']/div"
        products = self.driver.find_elements_by_xpath(f"{prod}/h4")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for product in products:
            if product.text == "Blackberry":
                product.find_element_by_xpath(f"{prod}/button").click()

        self.driver.find_element_by_partial_link_text("Checkout").click()
        self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("Uni")
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "United Kingdom")))

        self.driver.find_element_by_link_text("United Kingdom").click()
        self.driver.find_element_by_class_name("checkbox-primary").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        txt = self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in txt

        now_time = time.strftime('%Y-%m-%d %H-%M-%S')
        print(now_time)
        self.driver.get_screenshot_as_file(f'../picture/{now_time}.png')

        time.sleep(2)