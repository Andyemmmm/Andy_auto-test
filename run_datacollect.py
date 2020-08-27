"""统一运行入口"""
import argparse
import unittest
import HTMLReport
from EleganceReport import EleganceReport

from Common.tools.rw_ini import write_config

from Test_Suite.datacollect import suite_datacollect

# 从命令行读取参数修改配置文件
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

'''数据打点---停留事件的测试套件'''
suite.addTests(suite_datacollect.remain_event())
'''数据打点---聚合医疗平台首页点击事件的测试套件'''
suite.addTests(suite_datacollect.iwask_home_click_event())
'''数据打点---聚合医疗平台列表页点击事件的测试套件'''
suite.addTests(suite_datacollect.iwask_list_click_event())
'''数据打点---聚合医疗平台医生详情页点击事件的测试套件'''
suite.addTests(suite_datacollect.iwask_doctorinfo_click_event())
'''数据打点---聚合医疗平台套壳分享页点击事件的测试套件'''
suite.addTests(suite_datacollect.iwask_share_click_event())
'''数据打点---聚合医疗平台医生详情页点击事件的测试套件'''
suite.addTests(suite_datacollect.iwask_operationtopic_click_event())

'''报告模板1'''
# HTMLReport.TestRunner(
#     title="数据打点自动化测试",
#     description="数据打点",
#     report_file_name="index",
#     thread_count=1
# ).run(suite)

'''报告模板2'''
result = EleganceReport(suite)
result.report(filename='测试报告', description='聚合医疗平台数据打点测试报告', report_dir='report', theme='theme_memories')
