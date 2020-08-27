#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 16:53
# @File     : suite_updatearticle.py
# @Software : aiwen_ui

import unittest
from Test_Case.doctorClient import test_updatearticle
from Test_Case.communityClient.Application import test_science_project
from Test_Case.communityClient.Application import test_Health_science


def get_suite_health_science():
    """组织测试用例---社区活动--科普文章邀约写文章的交互流程"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_Health_science.Test_New_articles_invite))
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle))
    suite.addTests(loader.loadTestsFromTestCase(test_Health_science.Test_Filter_paper))

    return suite


def get_suite_science_project():
    """组织测试用例---社区活动--专题邀约写文章的交互流程"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_science_project.Test_New_Project_doctor))
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle))
    suite.addTests(loader.loadTestsFromTestCase(test_science_project.Test_Filter_paper))

    return suite


def get_suite_health():
    '''新建健康科普文章的流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle_health))

    return suite


def get_suite_clinic_and_diary():
    '''医生写诊间日记的流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle_Clinic_and_diary))

    return suite


def get_suite_case_analysis():
    '''医生写病例分析的流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle_case_analysis))

    return suite
