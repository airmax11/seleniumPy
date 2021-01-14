from selenium.webdriver.common.by import By
from Demo.pageobject.CheckOutPage import CheckOutPageObject


class ProductPageObject:
    prod = "//div[@class='card h-100']/div"
    product = (By.XPATH, f"{prod}/h4")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def prod_buttons_list(self):
        return self.driver.find_elements(*ProductPageObject.product)

    # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    def concr_prod_click(self, products):
        for product in products:
            if product.text == "Blackberry":
                product.find_element_by_xpath(f"{ProductPageObject.prod}/button").click()
                checkout = CheckOutPageObject(self.driver, self.wait)
                return checkout