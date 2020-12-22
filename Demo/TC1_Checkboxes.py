from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(1)


lst = driver.find_elements_by_css_selector("input[type='checkbox']")
lst2 = driver.find_element_by_css_selector("input[type='checkbox']")
print(len(lst))


for i in lst:
    i.click()
    print(i.get_attribute("value"))
    print(i.is_selected())
    assert i.is_selected()


lst_radio = driver.find_elements_by_css_selector("input[type='radio']")
lst_radio[2].click()

driver.find_element_by_css_selector("input[id='name']").send_keys("Test123")
driver.find_element_by_css_selector("input[type='submit'][value='Alert']").click()
alert = driver.switch_to.alert
txt = alert.text
alert.accept()

assert "Test123" in txt


time.sleep(1)

driver.close()
