"""
运行文件，引入测试套件TestSuite来批量运行测试用例，并生成测试报告
"""
# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport

from script.IHRM_Department import IHRMDepart

# 2.实例化测试套件
suite = unittest.TestSuite()
# 3.添加测试类
suite.addTest(unittest.makeSuite(IHRMDepart))
# 4.利用beatuifulReport生成测试报告
# filename = "depaetment_report{}".format(time.strftime("%Y-%m-%d %H%M%S"))
filename = "report.html"
BeautifulReport(suite).report(filename=filename, description="IHRM部门系统测试报告", log_path="../report")
