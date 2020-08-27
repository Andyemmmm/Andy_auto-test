#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 16:09
# @File     : run_admin.py
# @Software : aiwen_ui

import unittest
from BeautifulReport import BeautifulReport
import HTMLReport
from EleganceReport import EleganceReport
from Test_Suite.adminClient import suite_login, suite_content, suite_community, suite_audit

suite = unittest.TestSuite()  # 总的测试套件

# 医端的测试套件
# suite.addTests(suite_login.get_suite())
# suite.addTests(suite_content.article_detail())
# suite.addTests(suite_content.article_detail_del())
suite.addTests(suite_community.down_online_community())
suite.addTests(suite_community.up_online_community())
# suite.addTests(suite_audit.Review_community())
# suite.addTests(suite_audit.Online_application())

# HTMLReport.TestRunner(
#     title="爱问后台自动化测试",
#     description="爱问大后台 web ui 自动化测试",
#     report_file_name="index",
#     thread_count=1
# ).run(suite)
result = EleganceReport(suite)
result.report(filename='测试报告', description='爱问后台测试报告', report_dir='report', theme='theme_memories')
