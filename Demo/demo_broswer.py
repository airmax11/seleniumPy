from selenium import webdriver
from time import sleep as driver_sleep

driver = webdriver.Chrome(executable_path="c:\chromedriver_win32\chromedriver.exe")

# driver.get("https://rahulshettyacademy.com/")
# title = driver.title
# print(title)
# print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)
# print(driver.current_url)
# driver.back()
# driver.refresh()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("AirMax")
driver.find_element_by_name("email").send_keys("Yo")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
text = driver.find_element_by_class_name("alert-success").text
print(text)
assert "success" in text
driver_sleep(2)



driver.close()