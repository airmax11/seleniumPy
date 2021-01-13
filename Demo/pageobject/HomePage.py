from selenium.webdriver.common.by import By


class HomePageObject:
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self, driver):
        self.driver = driver

    def shop_button_click(self):
        self.driver.find_element(*HomePageObject.shop).click()