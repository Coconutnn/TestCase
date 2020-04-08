import os
import time

from selenium import webdriver

driver = webdriver.Chrome()
file_path='file:///'+os.path.abspath("E:\测试网页\drop_down.html")
driver.get(file_path)
time.sleep(2)
ship=driver.find_element_by_id("ShippingMethod")
ship.find_element_by_xpath("//*[@value='10.69']").click()
time.sleep(6)
driver.quit()