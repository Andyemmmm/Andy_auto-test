import unittest
from Test_Case.communityClient.Community import test_user


def get_suite():
    '''组织测试用例---用户模块---标签管理的新建标签流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_user.Test_New_label_management))
    return suite
