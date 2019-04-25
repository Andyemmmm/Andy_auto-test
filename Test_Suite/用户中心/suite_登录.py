import unittest
from Test_Case.用户中心 import test_login, test_login_ddt, test_login_ddt_file, test_login_log, test_login_封装, test_login_po


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # suite.addTests(loader.loadTestsFromTestCase(test_login.TestLogin))
    # suite.addTests(loader.loadTestsFromTestCase(test_login_ddt.TestLogin))
    # suite.addTests(loader.loadTestsFromTestCase(test_login_ddt_file.TestLogin))
    # suite.addTests(loader.loadTestsFromTestCase(test_login_log.TestLogin))
    # suite.addTests(loader.loadTestsFromTestCase(test_login_封装.TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(test_login_po.TestLogin))

    return suite
