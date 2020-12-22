from selenium import webdriver
from time import sleep as driver_sleep

driver = webdriver.Chrome(executable_path="c:\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
driver_sleep(2)
list_with_options = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
for i in list_with_options:
    if i.text == "India":
        i.click()
        break
driver_sleep(2)
print(driver.find_element_by_id("autosuggest").get_attribute("value"))
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"

driver.close()
