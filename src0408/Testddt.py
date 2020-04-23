from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os,sys,csv
from ddt import ddt, data, unpack ,file_data

def getCsv(file_name):
     rows=[]
     path=sys.path[0].replace('\test','')
     print(path)
     with open(path+'/data/'+file_name,'rt') as f:
         readers=csv.reader(f,delimiter=',',quotechar='|')
         next(readers,None)
         for row in readers:
             temprows=[]
             for i in row:
                temprows.append(i)
             rows.append(temprows)
         return rows
#引入ddt
@ddt
class Testddt(unittest.TestCase):
     def setUp(self):
         self.driver = webdriver.Firefox()
         self.driver.implicitly_wait(30)
         self.base_url = "http://www.baidu.com"
         self.verificationErrors = []
         self.accept_next_alert = True
 #测试用例，必须以test开头
 #增加ddt数据
 #@data('selenium',u'测试中文','9999999999')
 #@data(2,3,4)
 #单变更时不使用unpack
 #@data([3, 2], [4, 3], [5, 3])
     @data(*getCsv('test_baidu_data.csv'))
     #使用file_data需要在cmd窗口下运行，否则找不到文件
     #@file_data('test_data_list.json')
     @unpack
     def test_hao(self,value,expected_value):
     #def test_hao(self,value):
         driver = self.driver
         driver.get(self.base_url + "/")
         driver.find_element_by_id("kw").clear()
         driver.find_element_by_id("kw").send_keys(value)
         driver.find_element_by_id("su").click()
         time.sleep(2)
         self.assertEqual(expected_value, driver.title)
         print (expected_value)
         print (driver.title)
 #判断element是否存在，可删除
     def is_element_present(self, how, what):
         try: self.driver.find_element(by=how, value=what)
         except NoSuchElementException as e: return False
         return True
 #判断alert是否存在，可删除
     def is_alert_present(self):
         try: self.driver.switch_to.alert()
         except NoAlertPresentException as e: return False
         return True
 #关闭alert，可删除
     def close_alert_and_get_its_text(self):
         try:
             alert = self.driver.switch_to_alert()
             alert_text = alert.text
             if self.accept_next_alert:
                 alert.accept()
             else:
                 alert.dismiss()
             return alert_text
         finally: self.accept_next_alert = True
 #test fixture，清除环境
     def tearDown(self):
         self.driver.quit()
         self.assertEqual([], self.verificationErrors)
     def savescreenshot(self,driver,file_name):
         if not os.path.exists('./image'):
             os.makedirs('./image')
         now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
         #截图保存
         driver.get_screenshot_as_file('./image/'+now+'-'+file_name)
         time.sleep(1)
if __name__ == "__main__":
#执行用例
 unittest.main()