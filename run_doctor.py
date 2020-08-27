#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/4 8:49
# @File     : run_doctor.py
# @Software : aiwen_ui

import unittest
import HTMLReport

from Test_Suite.doctorClient import suite_updatearticle, suite_login

suite = unittest.TestSuite()  # 总的测试套件

# 医端的测试套件
# suite.addTests(suite_login.get_suite())
# suite.addTests(suite_updatearticle.get_suite_science_project())
# suite.addTests(suite_updatearticle.get_suite_health_science())
suite.addTests(suite_updatearticle.get_suite_health())
# suite.addTests(suite_updatearticle.get_suite_clinic_and_diary())
# suite.addTests(suite_updatearticle.get_suite_case_analysis())


HTMLReport.TestRunner(
    title="医端自动化测试",
    description="医端 web ui 自动化测试",
    report_file_name="index",
    thread_count=1
).run(suite)
