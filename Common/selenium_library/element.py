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
