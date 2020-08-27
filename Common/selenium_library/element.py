import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
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

    def send_element_key(self, locator, *value):
        """发送文本到元素上并点击
        :param locator: 元素定位方式
        :return:
        """
        self.logger.info(f"点击元素：{locator}")
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(*value)
        ele.send_keys(Keys.ENTER)

    def send_keys(self, locator, *value):
        """清空原有内容，发送文本或按键到元素上"""
        self.logger.info(f"发送文本或按键：{value} 到元素上：{locator}")
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(*value)

    def send_png(self, locator, *value):
        """发送文本或图片到元素上"""
        self.logger.info(f"发送文本或按键：{value} 到元素上：{locator}")
        ele = self.find_element(locator)
        ele.send_keys(*value)

    def switch_to_frame(self, locator):
        self.logger.info(f'跳转到{locator}')
        self.driver.switch_to.frame(locator)

    def switch_back_frame(self):
        self.logger.info('跳转回来')
        self.driver.switch_to.default_content()
        return self

    def by_offset(self, locator):
        self.logger.info(f'拉动元素{locator}往右偏移80个像素')
        ele = self.find_element(locator)
        ActionChains(self.driver).drag_and_drop_by_offset(ele, 80, 0).perform()

    def ex_script(self, locator):
        """执行脚本"""
        self.logger.info(f"滑动屏幕，直至到可见元素：{locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # self.driver.execute_script("arguments[0].click()", element)
        return self

    def ex_script_click(self, locator):
        """执行脚本"""
        self.logger.info(f"执行js脚本点击元素：{locator}")
        element = self.find_element(locator)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click()", element)
        return self

    def mouse_over(self, locator):
        """鼠标悬浮在元素上"""
        self.logger.info(f"鼠标悬浮在元素上：{locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def mouse_over_click(self, locator):
        """鼠标悬浮在元素上点击"""
        self.logger.info(f"鼠标悬浮在元素上点击：{locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

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

    def get_page_size(self, totalTtems, pagesize=10):
        '''
        页面的页码信息
        :param totalTtems: 记录总数
        :param pagesize: 分页大小
        :return:
        '''
        totalitem = self.find_element(totalTtems).text
        totalitem=totalitem[2:4]
        # pagesize = self.find_element(pagesize).text
        totalpage = math.ceil(int(totalitem) / int(pagesize))
        self.logger.info(f"返回总页数:{totalpage}")
        return totalpage

    def operate_page(self, totalpage, nextpage):
        if totalpage == 1:
            self.logger.info("当前只有一页，无需翻页处理")
        else:
            self.logger.info(f"当前共有{totalpage}页，可以翻页处理")
            for i in range(totalpage):
                self.find_element(nextpage).click()
                self.logger.info(f"开始翻页，第{i}次翻页")
