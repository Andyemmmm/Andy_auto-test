import unittest
from Test_Case.communityClient.Community import test_setting


def add_members():
    '''组织测试用例---设置模块---成员管理的添加成员流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_setting.Test_Add_members))
    return suite


def remove_members():
    '''组织测试用例---设置模块---成员管理的移除成员流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_setting.Test_Remove_members))
    return suite


def new_role():
    '''组织测试用例---设置模块---角色管理的新增角色流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_setting.Test_New_role))
    return suite


def del_role():
    '''组织测试用例---设置模块---角色管理的删除角色流程'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_setting.Test_Del_role))
    return suite
