import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:\\测试网页\\upload.html")
driver.get(file_path)
driver.implicitly_wait(10)
# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys("E:\\java_image_server\\images\\01.jpg")
time.sleep(3)
driver.quit()