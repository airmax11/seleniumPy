from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("AirMax")
driver.find_element_by_name("email").send_keys("airmax@gala.net")
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
time.sleep(2)



driver.close()