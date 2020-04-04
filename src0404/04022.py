from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
data = driver.find_element_by_name("tj_trnews").text
print(data)

# driver.find_element_by_id("kw").send_keys("金士杰")
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("谢可寅")
# driver.find_element_by_id("su").submit()
time.sleep(8)
driver.quit()