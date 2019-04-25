# https://docs.python.org/3/library/unittest.html
import unittest
from demo.unittest_demo import unitest_demo_1, unitest_demo_2
import HTMLReport

suite = unittest.TestSuite()  # 创建一个测试套件
loader = unittest.TestLoader()  # 创建一个测试用例加载器

# 将测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(unitest_demo_1.TestDemo))
suite.addTests(loader.loadTestsFromTestCase(unitest_demo_2.TestDemo))
# 从模块找用例类
# suite.addTests(loader.loadTestsFromModule(unitest_demo_1))
# 自动遍历目录寻找测试模块
# suite.addTests(loader.discover('.', pattern="*.py"))

# 运行并生成报告
HTMLReport.TestRunner(
    report_file_name="index",
    title="测试报告XXXX",
    description="参与人员。。。。XXX项目。。。"
).run(suite)
