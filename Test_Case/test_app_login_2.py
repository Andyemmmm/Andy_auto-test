import time
import unittest
from appium import webdriver
from HTMLReport import logger, AddImage

from Business.url import appium_url, dsc_app_index
from Common.dc import desired_capabilities


class TS_login(unittest.TestCase):
    def setUp(self):
        logger().info(f"连接appium服务器\n{appium_url}\n{desired_capabilities}")
        self.driver = webdriver.Remote(
            command_executor=appium_url,
            desired_capabilities=desired_capabilities
        )
        self.driver.implicitly_wait(5)
        AddImage(self.driver.get_screenshot_as_base64())
        pass

    def tearDown(self):
        logger().info("断开appium服务器")
        self.driver.quit()
        pass

    def test_login(self):
        username = "liu01"
        password = "123456"
        driver = self.driver
        logger().info("进入菜单栏")
        driver.find_element_by_accessibility_id("打开导航抽屉").click()
        logger().info("选择大商创")
        driver.find_element_by_xpath("//*[@text='大商创']").click()
        # 获取导航标题的文本值
        text = driver.find_element_by_xpath(
            "//*[@resource-id='io.github.liushilive.at:id/toolbar']/android.widget.TextView"
        ).text
        if "设置" == text:
            logger().info("设置服务器IP")
            driver.find_element_by_id("edit_ip").send_keys(dsc_app_index)
            logger().info("保存")
            driver.find_element_by_id("save").click()
            logger().info("进入菜单栏")
            driver.find_element_by_accessibility_id("打开导航抽屉").click()
            logger().info("选择大商创")
            driver.find_element_by_xpath("//*[@text='大商创']").click()

        logger().info("进入webview")
        driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
        time.sleep(2)
        logger().info("点击我")
        driver.find_element_by_xpath("//*[text()='我']/../a").click()
        logger().info("输入账号")
        driver.find_element_by_name("username").send_keys(username)
        logger().info("输入密码")
        driver.find_element_by_name("password").send_keys(password)
        logger().info("点击立即登录")
        driver.find_element_by_class_name("btn-submit").click()

        logger().info("断言登录成功")
        time.sleep(2)
        self.assertEqual("首页", driver.title)
        pass

    def test_login_密码错误(self):
        username = "liu01"
        password = "1234567"
        driver = self.driver
        logger().info("进入菜单栏")
        driver.find_element_by_accessibility_id("打开导航抽屉").click()
        logger().info("选择大商创")
        driver.find_element_by_xpath("//*[@text='大商创']").click()
        # 获取导航标题的文本值
        text = driver.find_element_by_xpath(
            "//*[@resource-id='io.github.liushilive.at:id/toolbar']/android.widget.TextView"
        ).text
        if "设置" == text:
            logger().info("设置服务器IP")
            driver.find_element_by_id("edit_ip").send_keys(dsc_app_index)
            logger().info("保存")
            driver.find_element_by_id("save").click()
            logger().info("进入菜单栏")
            driver.find_element_by_accessibility_id("打开导航抽屉").click()
            logger().info("选择大商创")
            driver.find_element_by_xpath("//*[@text='大商创']").click()

        logger().info("进入webview")
        driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
        time.sleep(2)
        logger().info("点击我")
        driver.find_element_by_xpath("//*[text()='我']/../a").click()
        logger().info("输入账号")
        driver.find_element_by_name("username").send_keys(username)
        logger().info("输入密码")
        driver.find_element_by_name("password").send_keys(password)
        logger().info("点击立即登录")
        driver.find_element_by_class_name("btn-submit").click()

        logger().info("断言登录失败")
        time.sleep(2)
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("用户名或密码错误", text)

        # for i in range(10):
        #     page = driver.page_source
        #     if "用户名或密码错误" in page:
        #         break
        #     time.sleep(500)
        # else:
        #     self.assertTrue(False, "页面没有出现 用户名或密码错误")

        pass

    def test_login_密码为空(self):
        username = "liu01"
        password = ""
        driver = self.driver
        logger().info("进入菜单栏")
        driver.find_element_by_accessibility_id("打开导航抽屉").click()
        logger().info("选择大商创")
        driver.find_element_by_xpath("//*[@text='大商创']").click()
        # 获取导航标题的文本值
        text = driver.find_element_by_xpath(
            "//*[@resource-id='io.github.liushilive.at:id/toolbar']/android.widget.TextView"
        ).text
        if "设置" == text:
            logger().info("设置服务器IP")
            driver.find_element_by_id("edit_ip").send_keys(dsc_app_index)
            logger().info("保存")
            driver.find_element_by_id("save").click()
            logger().info("进入菜单栏")
            driver.find_element_by_accessibility_id("打开导航抽屉").click()
            logger().info("选择大商创")
            driver.find_element_by_xpath("//*[@text='大商创']").click()

        logger().info("进入webview")
        driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
        time.sleep(2)
        logger().info("点击我")
        driver.find_element_by_xpath("//*[text()='我']/../a").click()
        logger().info("输入账号")
        driver.find_element_by_name("username").send_keys(username)
        logger().info("输入密码")
        driver.find_element_by_name("password").send_keys(password)
        logger().info("点击立即登录")
        driver.find_element_by_class_name("btn-submit").click()

        logger().info("断言登录失败")
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("请输入密码", text)
        pass
