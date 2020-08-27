#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/11 9:39
# @File     : debug.py
# @Software : aiwen_ui

import unittest
from EleganceReport import EleganceReport
import HTMLReport
from Common.tools.rw_ini import write_config

from Test_Suite.communityClient.用户中心 import suite_登录, suite_医生
from Test_Suite.communityClient.Application import suite_science_project, suite_network_bbs, suite_questionnaire, \
    suite_hospital, suite_doctor_class, suite_health_knowledge, suite_information, suite_健康科普
from Test_Suite.communityClient.Community import suite_community, suite_finance, suite_user, suite_setting, \
    suite_new_community, suite_bseting

suite = unittest.TestSuite()  # 总的测试套件
suite.addTests(suite_new_community.new_community_hoapital())

'''报告模板'''
# result = EleganceReport(suite)
# result.report(filename='测试报告', description='爱问后台测试报告', report_dir='report', theme='theme_memories')
