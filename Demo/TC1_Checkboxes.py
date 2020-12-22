from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)


driver.find_elements_by_css_selector("input[type='checkbox']").click()
