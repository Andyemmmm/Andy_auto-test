"""统一运行入口"""
import argparse
import unittest
import HTMLReport
from EleganceReport import EleganceReport

from Common.tools.rw_ini import write_config
from Test_Suite.用户中心 import suite_登录,suite_注册

# 从命令行读取参数修改配置文件
from Test_Suite.订单中心 import suite_购物车

parser = argparse.ArgumentParser(
    description="运行测试"  # 用来说明这个程序在做什么
)
parser.add_argument("-name", dest="name",
                    choices={"chrome", "firefox", "ie"}, default=None,
                    help="浏览器名字")
args = parser.parse_args()

if args.name is not None:
    write_config("Config/browser.ini", "browser", "name", args.name)

suite = unittest.TestSuite()  # 总的测试套件

# 将各个组装好的测试套件加入总的测试套件中
suite.addTests(suite_登录.get_suite())
# suite.addTests(suite_注册.get_suite())
# suite.addTests(suite_购物车.get_suite())


# HTMLReport.TestRunner(
#     title="大商创自动化测试报告",
#     description="大商创 web ui 自动化测试",
#     report_file_name="index",
#     thread_count=1
# ).run(suite)

'''报告模板2'''
result = EleganceReport(suite)
result.report(filename='测试报告', description='爱问后台测试报告', report_dir='report', theme='theme_memories')
