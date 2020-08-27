from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_ApplicationMarket(SeleniumBase):
    '''这个是社区--应用市场页面'''
    loc_调查问卷 = (By.XPATH, '//*[@id="5cfe12f1c91acd6b1163cf18"]/div[2]/p[1]')
    loc_医院推荐 = (By.XPATH, '//*[@id="5cfe1393c91acd6b1163cf1a"]/div[2]/p[1]')
    loc_医生课堂 = (By.XPATH, '//*[@id="5cfe142ac91acd6b1163cf1c"]/div[2]/p[1]')



    def click_调查问卷(self):
        self.mouse_over_click(self.loc_调查问卷)

    def click_医院推荐(self):
        self.mouse_over_click(self.loc_医院推荐)

    def click_医生课堂(self):
        self.mouse_over_click(self.loc_医生课堂)
