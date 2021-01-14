from selenium.webdriver.common.by import By
from Demo.pageobject.ProductPage import ProductPageObject


class HomePageObject:
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def shop_button_click(self):
        self.driver.find_element(*HomePageObject.shop).click()
        prodpage = ProductPageObject(self.driver, self.wait)
        return prodpage