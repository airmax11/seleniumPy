from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ADD_BUTTON = "//button[@type='button' and contains(text(), 'ADD TO CART')]"

def wair_for_severasl_elements(counter, xpath):
    cnt = 0
    while True:
        lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        if len(lst) == counter:
            break
        cnt += 1
        if cnt == 5:
            driver.close()
            raise RuntimeError
        continue

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
# driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.find_element_by_css_selector("input[type='search']").send_keys('be')
# buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
wair_for_severasl_elements(5, ADD_BUTTON)
# wait.until(EC.visibility_of_all_elements_located((By.XPATH, ADD_BUTTON)))
buttons = driver.find_elements_by_xpath("//button[@type='button' and contains(text(), 'ADD TO CART')]")

print(len(buttons))

for i in buttons:
    i.click()


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[@type='button' and text()='PROCEED TO CHECKOUT']").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
assert driver.find_element_by_css_selector("span.promoInfo").text == "Code applied ..!"

sleep(2)
driver.close()