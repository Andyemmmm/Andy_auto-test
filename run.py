import HTMLReport
import unittest
from Test_Suite import suite_ranzhi, suite_dsc_api

suite = unittest.TestSuite()

# suite.addTests(suite_ranzhi.get_suite())
suite.addTests(suite_dsc_api.get_suite())

HTMLReport.TestRunner(
    report_file_name="index",
    title="API 接口测试"
).run(suite)
