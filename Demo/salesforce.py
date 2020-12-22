from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
driver.get("https://login.salesforce.com/")

text = driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)")
print(text.text)
time.sleep(2)
driver.close()