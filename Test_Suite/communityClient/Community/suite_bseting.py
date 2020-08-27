import unittest
from Test_Case.communityClient.Community import test_bseting


def organization_update_name():
    '''组织测试用例---机构设置---更新机构名称流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_bseting.Test_organization_update_name))
    return suite


def Add_members():
    '''组织测试用例---添加机构成员---添加员工流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_bseting.Test_Add_members))
    return suite


def remove_members():
    '''组织测试用例---添加机构成员---移除员工流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_bseting.Test_remove_members))
    return suite


def update_personal():
    '''组织测试用例---个人信息---更新个人资料流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_bseting.Test_update_personal))
    return suite


def change_password():
    '''组织测试用例---安全设置---修改密码流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_bseting.Test_change_password))
    return suite
