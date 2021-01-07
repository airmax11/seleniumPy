from Demo.imp import prec as dr
PATH = "http://the-internet.herokuapp.com/iframe"

dr.navi(PATH)

text = dr.driver.find_element_by_css_selector("div[class='example'] h3").text
print(text)
dr.driver.switch_to.frame("mce_0_ifr")
dr.driver.find_element_by_id("tinymce").clear()
dr.driver.find_element_by_id("tinymce").send_keys(text + ".")
dr.sleep(2)
dr.driver.switch_to.default_content()
print(dr.driver.find_element_by_css_selector("div[class='example'] h3").text)
dr.driver.close()



