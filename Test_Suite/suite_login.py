import unittest
from Test_Case import test_app_login_1, test_app_login_2


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # suite.addTests(loader.loadTestsFromTestCase(test_app_login_1.TS_login))
    suite.addTests(loader.loadTestsFromTestCase(test_app_login_2.TS_login))

    return suite
