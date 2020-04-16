import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:\\测试网页\\alert.html")
driver.get(file_path)
# 点击链接弹出alert
driver.find_element_by_id("tooltip").click()
time.sleep(6)
# 得到文本信息打印
alert = driver.switch_to.alert
print(alert.text)
# 接受警告信息
# alert.dismiss()
alert.accept()
time.sleep(3)
driver.quit()