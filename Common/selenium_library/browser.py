from selenium import webdriver

from Common.selenium_library.base import Base
from Common.tools.rw_ini import read_config
from selenium.webdriver.chrome.options import Options


class Browser(Base):
    def get_web_driver(self):
        """获取一个浏览器"""
        # driver = webdriver.Chrome()
        rc = read_config("Config/browser.ini")
        devices = rc.getboolean("device", "devices")
        mobile_emulation = rc.get("device", "mobile_emulation")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', eval(mobile_emulation))
        local_browser = rc.getboolean("local", "local_browser")
        wait_time = rc.getint("local", "wait_time")
        browser_name = rc.get("browser", "name")
        ip = rc.get("remote", "hub")
        ports = rc.get("remote", "ports")
        headless = rc.get("remote", "headless")
        command_executor = f"http://{ip}:{ports}/wd/hub"
        if local_browser:
            # 本地浏览器
            if devices:
                driver = self._get_local_web_driver(browser_name, options)
            else:
                driver = self._get_local_web_driver(browser_name)
        else:
            # 远程浏览器
            if devices:
                driver = self._get_remote_web_driver(browser_name, command_executor, headless, mobile_emulation)
            else:
                driver = self._get_remote_web_driver(browser_name, command_executor, headless)

        self.logger.info(f"打开浏览器：{driver.name}")

        self.logger.info(f"设置隐式等待 {wait_time}s")
        driver.implicitly_wait(wait_time)

        self.logger.info("最大化浏览器")
        driver.maximize_window()

        return driver

    def _get_remote_web_driver(self, name, command_executor, headless, mobile_emulation=None):
        if name.upper() == "CHROME":
            if mobile_emulation:
                options = webdriver.ChromeOptions()
                options.add_experimental_option('mobileEmulation', eval(mobile_emulation))
            else:
                options = webdriver.ChromeOptions()
            # desired_capabilities = webdriver.DesiredCapabilities.CHROME
        elif name.upper() == "FIREFOX":
            options = webdriver.FirefoxOptions()
            # desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        elif name.upper() == "IE":
            options = webdriver.IeOptions()
            # desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        else:
            self.logger.info(f"浏览器类型错误：{name}")
            raise ValueError(f"浏览器类型错误：{name}")
        # 无头浏览器
        options.headless = headless
        driver = webdriver.Remote(
            command_executor=command_executor,
            # desired_capabilities=desired_capabilities,
            options=options
        )
        return driver

    def _get_local_web_driver(self, name: str, options=None):
        if name.upper() == "CHROME":
            if options:
                driver = webdriver.Chrome(chrome_options=options)
            else:
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
