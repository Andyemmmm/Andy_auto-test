import time

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Index(SeleniumBase):
    loc_请登录 = (By.LINK_TEXT, "请登录")
    loc_登陆后您好 = (By.XPATH, '//*[@id="ECS_MEMBERZONE"]/span[1]')
    loc_免费注册 = (By.LINK_TEXT, "免费注册")
    loc_我的购物车 = (By.XPATH, "//span[text()='我的购物车']/..")
    loc_购物车内商品数量 = (By.CSS_SELECTOR, ".header .cart_num")
    loc_移除购物车商品链接 = (By.CSS_SELECTOR, ".header .remove")
    loc_搜索框 = (By.ID, "keyword")
    loc_搜商品 = (By.CSS_SELECTOR, ".header .button-goods")

    def click_请登录链接(self):
        self.logger.info("点击请登录链接")
        self.click_element(self.loc_请登录)

    def get_登录成功提示您好(self):
        return self.get_element_text(self.loc_登陆后您好)

    def click_免费注册(self):
        self.click_element(self.loc_免费注册)
        pass

    def get_购物车内商品数量(self):
        return self.get_element_text(self.loc_购物车内商品数量)

    def click_移除购物车内所有商品(self):
        self.mouse_over(self.loc_我的购物车)
        while self.is_element(self.loc_移除购物车商品链接, 1):
            self.click_element(self.loc_移除购物车商品链接)
            time.sleep(1)

    def send_搜索商品(self, goods):
        self.send_keys(self.loc_搜索框, goods)

    def click_搜索商品按钮(self):
        self.click_element(self.loc_搜商品)
