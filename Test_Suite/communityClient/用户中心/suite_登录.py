import unittest
from Test_Case.communityClient.用户中心 import test_login_po


def login():
    """组织测试用例---登录的测试套件"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_login_po.TestLogin))

    return suite


def login_code():
    """组织测试用例---验证码登录的测试套件"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_login_po.TestLogin_code))

    return suite


def loginout():
    """组织测试用例---退出登陆的测试套件"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_login_po.Test_Loginout))

    return suite


def experience_community():
    """组织测试用例---登录的测试套件"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_login_po.Test_experience_community))

    return suite
