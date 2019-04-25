import unittest
from Test_Case.订单中心 import test_购物车


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_购物车.Test_购物车))
    return suite
