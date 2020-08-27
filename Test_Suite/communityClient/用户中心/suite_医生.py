import unittest
from Test_Case.communityClient.Community import test_doctor


def doctor_invite():
    """组织测试用例--医生模块---邀请医生加入社区"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test_doctor.TestDoctor))

    return suite


def label_management():
    """组织测试用例--医生模块--新建标签管理"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test_doctor.Test_Lable_Management))

    return suite
