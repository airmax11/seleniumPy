from Demo.imp import prec as dr
PATH = "https://rahulshettyacademy.com/AutomationPractice/"
dr.driver.maximize_window()
dr.navi(PATH)

dr.move_mouse_to_element("mousehover")
dr.mouse_click_on_element("Top")

dr.move_mouse_to_element("mousehover")
dr.mouse_click_on_element("Reload")

assert dr.driver.find_element_by_id("displayed-text").is_displayed()
print(dr.driver.find_element_by_id("displayed-text").is_displayed())
dr.driver.find_element_by_id("hide-textbox").click()

assert not dr.driver.find_element_by_id("displayed-text").is_displayed()
print(dr.driver.find_element_by_id("displayed-text").is_displayed())


dr.sleep(2)
dr.driver.close()