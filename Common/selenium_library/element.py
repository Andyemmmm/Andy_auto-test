from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Common.selenium_library.base import Base


class Element(Base):
    def get_element_text(self, locator):
        """获取元素的文本值

        :param locator: 元素的定位方式
        :return: 文本值
        """
        text = self.find_element(locator).text
        self.logger.info(f"获取元素的文本值：{text}")
        return text

    def click_element(self, locator):
        """点击元素

        :param locator: 元素定位方式
        :return:
        """
        self.logger.info(f"点击元素：{locator}")
        self.find_element(locator).click()

    def send_keys(self, locator, *value):
        """清空原有内容，发送文本或按键到元素上"""
        self.logger.info(f"发送文本或按键：{value} 到元素上：{locator}")
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(*value)

    def mouse_over(self, locator):
        """鼠标悬浮在元素上"""
        self.logger.info(f"鼠标悬浮在元素上：{locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def is_element(self, locator, time_out=0):
        """判断元素是否存在"""
        self.logger.info(f"判断页面是否存在元素：{locator}")
        try:
            # 显式等待
            WebDriverWait(self.driver, time_out).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.info("元素不存在")
            return False
        else:
            self.logger.info("元素存在")
            return True

    def get_element_attribute(self, locator, attribute):
        """返回元素的属性值"""
        if not attribute:
            raise ValueError("attribute 不能为空")
        attribute_text = self.find_element(locator).get_attribute(attribute)
        self.logger.info(f"返回元素 {locator} 的 {attribute} 属性值：{attribute_text}")
        return attribute_text
