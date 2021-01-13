import time

from Demo.utilities import prec as dr
PATH = "https://rahulshettyacademy.com/angularpractice/"

dr.navi(PATH)
dr.driver.find_element_by_link_text("Shop").click()

prod = "//div[@class='card h-100']/div"
products = dr.driver.find_elements_by_xpath(f"{prod}/h4")
# dr.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for product in products:
    if product.text == "Blackberry":
        product.find_element_by_xpath(f"{prod}/button").click()

dr.driver.find_element_by_partial_link_text("Checkout").click()
dr.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
dr.driver.find_element_by_id("country").send_keys("Uni")
dr.wait.until(dr.EC.presence_of_element_located((dr.By.LINK_TEXT, "United Kingdom")))

dr.driver.find_element_by_link_text("United Kingdom").click()
dr.driver.find_element_by_class_name("checkbox-primary").click()
dr.driver.find_element_by_css_selector("input[value='Purchase']").click()
txt = dr.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in txt

now_time = time.strftime('%Y-%m-%d %H-%M-%S')
print(now_time)
dr.driver.get_screenshot_as_file(f'./picture/{now_time}.png')


dr.sleep(2)
dr.driver.close()