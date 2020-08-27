#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 10:43
# @File     : suite_science_project.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_science_project
from Test_Case.doctorClient import test_updatearticle


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test_science_project.Test_New_Project_doctor))
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle))
    suite.addTests(loader.loadTestsFromTestCase(test_science_project.Test_Filter_paper))
    suite.addTests(loader.loadTestsFromTestCase(test_science_project.Test_Remove_the_projects))

    return suite
