import unittest
from selenium import webdriver


class TestDemo(unittest.TestCase):
    """测试用例类"""

    def setUp(self):
        """测试前执行"""
        self.driver = webdriver.Chrome()

    @unittest.skip("无条件跳过用例执行")
    def test_open_baidu(self):
        """测试用例"""
        self.driver.get("https://www.baidu.com")
        # 断言
        self.assertIn("百度", self.driver.title)

    def tearDown(self):
        """测试后执行"""
        self.driver.quit()

    def test_open_bing(self):
        """测试用例"""
        self.driver.get("https://www.bing.com")
        self.skipTest("运行中跳过")
        # 断言
        self.assertIn("Bing", self.driver.title)
