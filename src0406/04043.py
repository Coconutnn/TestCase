from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("清明节")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
# 全选 ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
# 剪切 ctrl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("杏花村")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()