from Demo.imp import prec as dr
PATH = "https://rahulshettyacademy.com/angularpractice/"

dr.navi(PATH)
dr.driver.find_element_by_link_text("Shop").click()

prod = "//div[@class='card h-100']/div"
products = dr.driver.find_elements_by_xpath(f"{prod}/h4")
# dr.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for product in products:
    if product.text == "Blackberry":
        print(product.find_element_by_xpath(f"{prod}/h5").text)
        product.find_element_by_xpath(f"{prod}/button").click()

dr.sleep(2)
dr.driver.close()