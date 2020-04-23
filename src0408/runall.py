import unittest, csv
import os, sys
import time


# 手工添加案例到套件，
from src0408 import HTMLTestRunner


def createsuite():
    # /src0408下的 以test开头  .py结尾的所有文件
    discover = unittest.defaultTestLoader.discover('../src0408', pattern='test*.py', top_level_dir=None)
    print (discover)
    return discover


if __name__ == "__main__":
    # sys.path是python搜索模块的路径集，返回的结果是一个List
    curpath = sys.path[0]
    print(sys.path)
    if not os.path.exists(curpath + '/resultreport'):
        os.makedirs(curpath + '/resultreport')
    # 取当前时间
    # strftime作用是格式化时间戳为本地的时间
    # time()函数用户返回当前时间的时间戳（1970年01月08时00分00秒到现在的浮点秒数）
    # localtime()函数的作用是格式化时间戳为本地struct_time；如果secs参数未输入则默认为当前时间
    # localtime()函数语法：time.localtime([secs])//time指的是time模块，可选参数secs表示1970-1-1到现在的秒数
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print(now)

    filename = curpath + '/resultreport/' + now + 'resultreport.html'
    with open(filename, 'wb') as fp:
    # 出html报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况',verbosity=2)
        suite = createsuite()
        runner.run(suite)