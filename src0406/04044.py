import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
file_path='file:///'+os.path.abspath("E:\测试网页\level_locate.html")
driver.get(file_path)
WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_link_text("Link1"))
# driver.implicitly_wait(10)
# 定位Link1的Action
driver.find_element_by_link_text("Link1").click()
list=driver.find_element_by_id("dropdown1").find_elements_by_link_text("Action")
webdriver.ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(6)
driver.quit()