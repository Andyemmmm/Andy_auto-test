import unittest
from test_suite import suite_user
import HTMLReport
# from loan_project.common import contants



# discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")
#
# with open(contants.report_dir + '/report.html', 'wb+') as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                               title="API TEST REPORT",
#                                               description="牙医管家",
#                                               tester="邓逸")
#     runner.run(discover)

suite=unittest.TestSuite()
suite.addTests(suite_user.get_suite())

HTMLReport.TestRunner(
    report_file_name='index',
    title='API TEST REPORT',
    description='牙医管家',

).run(suite)