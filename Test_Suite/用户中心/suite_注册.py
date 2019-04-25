import unittest
from Test_Case.用户中心 import test_register


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test_register.Test_Register))

    return suite
