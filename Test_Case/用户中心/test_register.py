import unittest
import ddt
from Business.base_url import url_index
from Business.用户中心.task_注册业务 import register
from Common.selenium_library import SeleniumBase
from Common.tools.random_text import get_rendom_username, get_random_phone
from Page_Object.page_index import Page_Index


@ddt.ddt
class Test_Register(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        SeleniumBase(self.driver).quit()
        pass

    @ddt.data(*get_rendom_username(5))
    def test_register(self, username):
        # username = "liu001"
        password = "123456"
        pwdRepeat = "123456"
        # mobile_phone = "13311111113"
        mobile_phone = get_random_phone()

        se = SeleniumBase(self.driver)
        se.logger.info("打开首页")
        se.get(url_index)
        se.logger.info("进入注册页")
        Page_Index(self.driver).click_免费注册()
        se.logger.info("注册流程")
        register(self.driver, username, password, pwdRepeat, mobile_phone)

        # 断言
        text = Page_Index(self.driver).get_登录成功提示您好()
        self.assertIn("您好", text)

        with open("Test_Data/user.txt", "a", encoding="utf-8") as f:
            f.write(f"{username}|{password}\n")
