import unittest
from Test_Case.communityClient.Community import test_community


def get_suite():
    '''社区管理---首页管理流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_community.Test_home_management))
    return suite
