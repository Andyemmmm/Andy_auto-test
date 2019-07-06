import unittest
from Test_Case import test_插入会员信息API


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_插入会员信息API.Test_插入会员信息API))

    return suite
