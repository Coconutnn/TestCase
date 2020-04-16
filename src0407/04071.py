from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:\\测试网页\\frame.html")
driver.get(file_path)
driver.maximize_window()
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("布拉格")
driver.find_element_by_id("su").click()
time.sleep(8)
# 让页面跳转回原来的默认页面
driver.switch_to.default_content()
driver.find_element_by_link_text("click").click()
time.sleep(6)
driver.quit()