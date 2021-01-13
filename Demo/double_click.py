from Demo.utilities import prec as dr
PATH = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"

dr.navi(PATH)
dr.double_click_on_element("#double-click")
print(dr.driver.switch_to.alert.text)
assert "You double clicked me!!!, You got to be kidding me" == dr.driver.switch_to.alert.text

dr.driver.switch_to.alert.accept()


dr.sleep(2)
dr.driver.close()