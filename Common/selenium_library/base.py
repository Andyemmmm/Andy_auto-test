from selenium import webdriver
from HTMLReport import logger


class Base(object):
    def __init__(self, driver: webdriver.Remote = None):
        self.driver = driver
        self.logger = logger()

    def find_element(self, locator: tuple):
        """查找元素

        :param locator: 定位器(by=By.ID, value=None)
        :return: web元素
        """
        self.logger.info(f"查找元素：{locator}")
        try:
            element = self.driver.find_element(*locator)
        except Exception:
            self.logger.info("查找元素失败")
            raise
        else:
            self.logger.info("查找元素成功")
        return element
