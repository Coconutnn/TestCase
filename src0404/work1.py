from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
time.sleep(2)
driver.find_element_by_id("switchAccountLogin").click()
time.sleep(5)
i = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(i)
driver.find_element_by_name("email").send_keys("x13345986135")
driver.find_element_by_name("password").send_keys("xukaini1204")
driver.find_element_by_id("dologin").click()
time.sleep(10)
driver.quit()