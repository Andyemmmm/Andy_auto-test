import unittest
import HTMLReport
from Test_Suite import suite_login

suite = unittest.TestSuite()

suite.addTests(suite_login.get_suite())

HTMLReport.TestRunner(
    title="APP",
    report_file_name="index",
    thread_count=3
).run(suite)
