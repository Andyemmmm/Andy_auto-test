import unittest
from Test_Case.communityClient.Community import test_new_community, test_home_page

'''社区B端---新建医院类型的社区'''


def new_community_hoapital():
    '''社区B端---新建医院类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_community_hospital))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建机构类型的社区'''


def new_community_organization():
    '''社区B端---新建机构类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_community_organization))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建医生团队类型的社区'''


def new_community_doctorteam():
    '''社区B端---新建医生团队类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_community_doctorteam))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建项目型社区'''


def new_community_project():
    '''社区B端---新建项目型社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_community_project))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''***********************新建测试类型的社区*****************************新建测试类型的社区******************************新建测试类型的社区********************************'''

'''社区B端---新建测试类型的医院类型的社区'''


def new_test_community_hoapital():
    '''社区B端---新建测试类型的医院类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_Test_community_hospital))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建测试类型的机构类型的社区'''


def new_test_community_organization():
    '''社区B端---新建测试类型的机构类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_Test_community_organization))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建测试类型的医生团队类型的社区'''


def new_test_community_doctorteam():
    '''社区B端---新建测试类型的医生团队类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_Test_community_doctorteam))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite


'''社区B端---新建测试类型的项目类型的社区'''


def new_test_community_project():
    '''社区B端---新建测试类型的项目类型的社区'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_new_community.Test_New_Test_community_project))
    suite.addTests((loader.loadTestsFromTestCase(test_new_community.Test_Review_community)))
    suite.addTests((loader.loadTestsFromTestCase(test_home_page.Test_up_online)))
    return suite
