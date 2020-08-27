import unittest
from Test_Case.communityClient.Application import test_Health_science
from Test_Case.doctorClient import test_updatearticle


def get_suite():
    """组织测试用例--健康科普---新建文章邀约和筛选文章流程"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(test_Health_science.Test_New_articles_invite))
    suite.addTests(loader.loadTestsFromTestCase(test_updatearticle.Test_Updatearticle))
    suite.addTests(loader.loadTestsFromTestCase(test_Health_science.Test_Filter_paper))
    return suite
