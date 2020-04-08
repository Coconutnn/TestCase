from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("清明节")
driver.find_element_by_id("su").click()
time.sleep(3)
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#将页面滚动条拖到顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
# 右击
su=driver.find_element_by_id("su")
ActionChains(driver).context_click(su).perform()

time.sleep(3)
driver.quit()
