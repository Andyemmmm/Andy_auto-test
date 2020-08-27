#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 19:36
# @File     : test_case.py
# @Software : aiwen_ui

import unittest
from EleganceReport import EleganceReport
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 2)

    @EleganceReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """

        self.assertIsNone(None)


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./tests', pattern='test*.py')
    result = EleganceReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', report_dir='report', theme='theme_default')
