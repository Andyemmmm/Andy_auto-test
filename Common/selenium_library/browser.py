from selenium import webdriver

from Common.selenium_library.base import Base
from Common.tools.rw_ini import read_config


class Browser(Base):
    def get_web_driver(self):
        """获取一个浏览器"""
        # driver = webdriver.Chrome()
        rc = read_config("Config/browser.ini")
        local_browser = rc.getboolean("local", "local_browser")
        wait_time = rc.getint("local", "wait_time")
        browser_name = rc.get("browser", "name")

        if local_browser:
            # 本地浏览器
            driver = self._get_local_web_driver(browser_name)
        else:
            # 远程浏览器
            pass

        self.logger.info(f"打开浏览器：{driver.name}")

        self.logger.info(f"设置隐式等待 {wait_time}s")
        driver.implicitly_wait(wait_time)

        self.logger.info("最大化浏览器")
        driver.maximize_window()

        return driver

    def _get_local_web_driver(self, name: str):
        if name.upper() == "CHROME":
            driver = webdriver.Chrome()
        elif name.upper() == "FIREFOX":
            driver = webdriver.Firefox()
        elif name.upper() == "IE":
            driver = webdriver.Ie()
        else:
            self.logger.info(f"浏览器类型错误：{name}")
            raise ValueError(f"浏览器类型错误：{name}")
        return driver

    def quit(self):
        """退出浏览器"""
        self.logger.info(f"关闭浏览器：{self.driver.name}")
        self.driver.quit()

    def get(self, url):
        """打开网址

        :param url: 网址
        :return:
        """
        self.logger.info(f"打开网址：{url}")
        self.driver.get(url)
