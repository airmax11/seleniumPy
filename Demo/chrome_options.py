from selenium import webdriver
PATH = "https://rahulshettyacademy.com/angularpractice/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe", options=chrome_options)

driver.get(PATH)

name_field = driver.find_element_by_name("name")
name_field.send_keys("Hello Max")
print(name_field.get_attribute("value"))

text = driver.execute_script("return document.getElementsByName('name')[0].value")
print(text)

shop_button = driver.find_element_by_link_text("Shop")
print(shop_button.text)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("arguments[0].click();", shop_button)
driver.close()


