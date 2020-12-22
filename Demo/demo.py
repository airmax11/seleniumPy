from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")


driver.get("https://www.amazon.de/")
time.sleep(2)
driver.maximize_window()
driver.find_element_by_id("twotabsearchtextbox").send_keys("kindle oasis 2020")
driver.find_element_by_css_selector("[value='Los']").click()
driver.find_element_by_partial_link_text("Kindle Oasis, Leselicht mit verstellbarer").click()
time.sleep(2)
print(driver.title)
print(driver.current_url)
test = driver.find_elements_by_xpath("//*[starts-with(text(),'Dieses')]")
print(test[0].text)
driver.find_element_by_xpath("//span[@class='a-size-base' and contains(text(), '32 GB WLAN + Gratis 4G')]").click()
print(driver.find_element_by_xpath("//span[@class='selection' and contains(text(), '32 GB WLAN + Gratis 4G')]").text)

driver.close()