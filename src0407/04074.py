import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:\测试网页\model.html")
driver.get(file_path)
driver.find_element_by_id("show_modal").click()
time.sleep(2)
driver.find_element_by_id("click").click()
time.sleep(2)
# 先定位div，再定位到button组
# buttons = driver.find_element_by_class_name("modal-footer").find_elements_by_tag_name("button")
# 如果页面只有一组button组（一个div里多个button），可以直接定位button，注意是elements
buttons = driver.find_elements_by_tag_name("button")
buttons[0].click()
time.sleep(3)
driver.quit()