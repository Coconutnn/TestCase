import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:\测试网页\send.html")
driver.get(file_path)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/input").click()
# 在弹出框输入内容
alert = driver.switch_to.alert
alert.send_keys("webdriver")
# 确定
alert.accept()
time.sleep(5)
driver.quit()
