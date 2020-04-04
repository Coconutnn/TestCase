from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)

# id,name,class都是css selector,前面要加#
driver.find_element_by_css_selector("#kw").send_keys("终南山")
driver.find_element_by_css_selector('#su').click()
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("孔雪儿")
# driver.find_element_by_xpath("//*[@id='su']").click()
# driver.find_element_by_partial_link_text("肺炎").click()
# driver.find_element_by_partial_link_text("抗击肺炎").click()
# 用name和id都可以定位
# driver.find_element_by_name("wd").send_keys("大鱼海棠")
# driver.find_element_by_id("kw").send_keys("赵小棠")
#driver.find_element_by_id("su").click()

time.sleep(6)
driver.quit()