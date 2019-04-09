"""统一运行入口"""
import unittest
import HTMLReport
from Test_Suite.用户中心 import suite_登录

suite = unittest.TestSuite()  # 总的测试套件

# 将各个组装好的测试套件加入总的测试套件中
suite.addTests(suite_登录.get_suite())

HTMLReport.TestRunner(
    title="大商创自动化测试报告",
    description="大商创 web ui 自动化测试",
    report_file_name="index"
).run(suite)






