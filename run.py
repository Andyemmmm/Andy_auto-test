import unittest
from test_suite import suite_user, suite_community_web
from test_suite.api import Online_class
import HTMLReport
from EleganceReport import EleganceReport
from common import HTMLTestRunnerNew

# from loan_project.common import contants

suite = unittest.TestSuite()
# suite.addTests(suite_user.get_suite())
suite.addTests(suite_community_web.get_suite())
# suite.addTests(Online_class.get_suite())


'''
*********************************************************************************
                    报告类型1
*********************************************************************************

'''
# suite=unittest.TestSuite()
# suite.addTests(suite_user.get_suite())
#
# HTMLReport.TestRunner(
#     report_file_name='index',
#     title='API TEST REPORT',
#     description='B端官网添加客户',
#
# ).run(suite)


'''
*********************************************************************************
                    报告类型2
*********************************************************************************
'''

# with open('report/test_result006.html', 'wb')as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(
#         stream=file,
#         title='社区接口-机构管理',
#         description='社区机构接口测试',
#         tester='曾润平'
#     )
#     runner.run(suite)

'''
*********************************************************************************
                    报告类型3
*********************************************************************************
'''
result = EleganceReport(suite)
result.report(filename='测试报告', description='社区web改版接口自动化测试报告', report_dir='report', theme='theme_memories')
