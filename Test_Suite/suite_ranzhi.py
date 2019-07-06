import unittest
from Test_Case import ranzhi_login


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(ranzhi_login.Ranzhi_login))

    return suite
