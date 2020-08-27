import unittest
from Test_Case.communityClient.Community import test_finance


def get_suite():
    '''组织测试用例---财务模块---金币充值流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_finance.Test_Finance))
    return suite
