from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()#浏览器最大化
driver.find_element_by_link_text("hao123").click()
#driver.implicitly_wait(10)
time.sleep(6)
#driver.set_window_size(400,800)#将浏览器缩小
driver.back()#浏览器后退
t = driver.title
print(t)
url = driver.current_url
print(url)
time.sleep(3)
driver.forward()#浏览器前进
driver.quit()