import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
# from Demo.imp import prec as dr
from Demo.pageobject.CheckOutPage import CheckOutPageObject
from Demo.pageobject.ProductPage import ProductPageObject
from Demo.utilities.BaseClass import Baseclass
from Demo.pageobject.HomePage import HomePageObject



class Testsuit_01(Baseclass):

    def test_e2e(self):
        homepage = HomePageObject(self.driver, self.wait)
        page_page = homepage.shop_button_click()
        prod_list = page_page.prod_buttons_list()
        checkout = page_page.concr_prod_click(prod_list)
        checkout.click_on_checkout_button()
        checkout.click_on_success_button()
        checkout.send_keys_to_country("Uni")
        checkout.wait_for_element("United Kingdom")
        checkout.checkbox_purchase()

        txt = self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in txt

        now_time = time.strftime('%Y-%m-%d %H-%M-%S')
        print(now_time)
        self.driver.get_screenshot_as_file(f'../picture/{now_time}.png')

        time.sleep(2)