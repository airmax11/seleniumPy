from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckOutPageObject:

    product = (By.PARTIAL_LINK_TEXT, "Checkout")
    success_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    country_field = (By.ID, "country")
    check_box_primary = (By.CLASS_NAME, "checkbox-primary")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_text = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")


    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_on_checkout_button(self):
        self.driver.find_element(*CheckOutPageObject.product).click()

    def click_on_success_button(self):
        self.driver.find_element(*CheckOutPageObject.success_button).click()

    def send_keys_to_country(self, keys):
        self.driver.find_element(*CheckOutPageObject.country_field).send_keys(keys)

    def checkbox_purchase(self):
        self.driver.find_element(*CheckOutPageObject.check_box_primary).click()
        self.driver.find_element(*CheckOutPageObject.purchase_button).click()

    def get_text(self):
        return self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
