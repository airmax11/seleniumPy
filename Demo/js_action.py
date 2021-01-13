from Demo.utilities import prec as dr
PATH = "https://rahulshettyacademy.com/angularpractice/"
dr.driver.set_window_size("800", "600")

dr.navi(PATH)


name_field = dr.driver.find_element_by_name("name")
name_field.send_keys("Hello Max")
print(name_field.get_attribute("value"))

text = dr.driver.execute_script("return document.getElementsByName('name')[0].value")
print(text)

shop_button = dr.driver.find_element_by_link_text("Shop")
print(shop_button.text)

dr.driver.execute_script("arguments[0].click();", shop_button)
dr.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

dr.sleep(2)
dr.driver.close()