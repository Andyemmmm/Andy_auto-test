from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Search(SeleniumBase):
    loc_第一个商品 = (By.XPATH, '//*[@class="gl-item"][1]//*[@class="p-name"]/a')
    loc_找不到商品提示 = (By.CSS_SELECTOR, ".no_info_line h3")

    def get_第一个商品文本(self):
        return self.get_element_attribute(self.loc_第一个商品, "title")

    def click_第一个商品(self):
        self.click_element(self.loc_第一个商品)

    def get_找不到商品提示(self):
        return self.get_element_text(self.loc_找不到商品提示)
