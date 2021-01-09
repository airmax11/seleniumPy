from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(executable_path="c:/webdirver/chromedriver.exe")
# driver.set_window_size("1920", "1080")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

def navi(path):
    driver.get(path)

def move_mouse_to_element(element):
    action.move_to_element(driver.find_element_by_id(element)).perform()

def mouse_click_on_element(element):
    action.move_to_element(driver.find_element_by_link_text(element)).click().perform()

def double_click_on_element(element):
    action.double_click(driver.find_element_by_css_selector(element)).perform()

def wair_for_several_elements(counter, xpath):
    cnt = 0
    while True:
        lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        if len(lst) >= counter:
            break

        if cnt == 5:
            driver.close()
            raise RuntimeError
        cnt += 1
        continue
