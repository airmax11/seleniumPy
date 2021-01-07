from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
wait = WebDriverWait(driver, 10)
driver.get("http://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
driver.switch_to.window(driver.window_handles[1])

assert "New Window" == driver.find_element_by_tag_name("h3").text
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

sleep(2)
driver.quit()