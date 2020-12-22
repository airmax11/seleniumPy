from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)


lst = driver.find_elements_by_css_selector("input[type='checkbox']")
lst2 = driver.find_element_by_css_selector("input[type='checkbox']")
print(len(lst))


for i in lst:
    i.click()
    print(i.is_selected())
    assert i.is_selected()

time.sleep(2)

driver.close()
