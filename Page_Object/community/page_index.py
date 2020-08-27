from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Index(SeleniumBase):
    '''这是社区B端的首页'''
    loc_登录 = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/a[2]')
    loc_加入我们 = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/a[1]')
    loc_免费试用 = (By.XPATH, '//*[@id="fullpage"]/div[1]/div/div/div[2]/a')
    loc_久久医康社区 = (By.XPATH, '//*[@id="fullpage"]/div[1]/div/div/div[2]/dl/dt')


    def click_登陆(self):
        self.logger.info("点击请登录")
        return self.click_element(self.loc_登录)

    def click_加入我们(self):
        self.click_element(self.loc_加入我们)
        return self

    def click_免费试用(self):
        self.click_element(self.loc_免费试用)


    def get_获取久久医康社区(self):
        return self.get_element_text(self.loc_久久医康社区)



    # def get_购物车内商品数量(self):
    #     return self.get_element_text(self.loc_购物车内商品数量)
    #
    # def click_移除购物车内所有商品(self):
    #     self.mouse_over(self.loc_我的购物车)
    #     while self.is_element(self.loc_移除购物车商品链接, 1):
    #         self.click_element(self.loc_移除购物车商品链接)
    #         time.sleep(1)
    #
    # def send_搜索商品(self, goods):
    #     self.send_keys(self.loc_搜索框, goods)
