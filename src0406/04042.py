from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #需要引入keys 包
import os
driver = webdriver.Chrome()
driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
driver.implicitly_wait(10)
driver.find_element_by_id("account").send_keys("admin")

driver.find_element_by_id("account").send_keys(Keys.TAB) # tab快捷键
driver.find_element_by_name("password").send_keys("xukaini1204")
driver.find_element_by_name("password").send_keys(Keys.ENTER)# 按回车快捷键
time.sleep(6)
driver.quit()