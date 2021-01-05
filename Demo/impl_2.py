from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ADD_BUTTON = "//div[@class='product-action']/button"

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

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
wair_for_several_elements(3, ADD_BUTTON)
buttons_go = driver.find_elements_by_xpath(ADD_BUTTON)
list_with_products = []

for i in buttons_go:
    list_with_products.append(i.find_element_by_xpath( "parent::div/parent::div/h4").text)
    i.click()

print(list_with_products)
driver.close()


