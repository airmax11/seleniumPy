from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ADD_BUTTON = "//div[@class='product-action']/button"
TOTAL_AMOUNT = "span.totAmt"
DISC_AMOUNT = "span.discountAmt"

def wair_for_several_elements(counter, xpath):
    cnt = 0
    while True:
        lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        if len(lst) == counter:
            break

        if cnt == 5:
            driver.close()
            raise RuntimeError
        cnt += 1
        continue

def calculate_discount(discount, amount):
    return amount - (amount / discount)


driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
wair_for_several_elements(3, ADD_BUTTON)
buttons_go = driver.find_elements_by_xpath(ADD_BUTTON)
list_with_products = []

for i in buttons_go:
    list_with_products.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[@type='button' and text()='PROCEED TO CHECKOUT']").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

table_values = "p.product-name"
list_with_items = [x.text for x in driver.find_elements_by_css_selector(table_values)]

totAmt = float(driver.find_element_by_css_selector(TOTAL_AMOUNT).text)
discAmt = float(driver.find_element_by_css_selector(DISC_AMOUNT).text)

assert list_with_items == list_with_products
assert driver.find_element_by_css_selector("span.promoInfo").text == "Code applied ..!"
assert discAmt == calculate_discount(10, totAmt)

# Check that SUM in table calculated correctly
# Check that Search on home page is working and Ber looking for 3 items


driver.close()


