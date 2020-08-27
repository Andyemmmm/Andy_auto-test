from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_MyApplication(SeleniumBase):
    '''这个是社区--应用模块页面'''
    loc_科普专题 = (By.XPATH, '//li[@id="5cfe0a59c91acd6b1163cf08"]/div[2]/p[1]')
    loc_咨询公告 = (By.XPATH, '//li[@id="5cfe0725c91acd6b1163cf06"]/div[2]/p[1]')
    loc_健康知识 = (By.XPATH, '//li[@id="5cfe068cc91acd6b1163cf04"]/div[2]/p[1]')
    loc_圈子论坛 = (By.XPATH, '//li[@id="5cfe05aec91acd6b1163cf02"]/div[2]/p[1]')
    loc_健康科普 = (By.XPATH, '//li[@id="5cfdf962c91acd6b1163cf00"]/div[2]/p[1]')
    loc_应用市场 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/span')
    loc_我的应用 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[1]/li/span')
    loc_医生课堂 = (By.XPATH, "//li[@id='5cfe142ac91acd6b1163cf1c']/div[2]/p[1]")
    loc_医院推荐 = (By.XPATH, '//li[@id="5cfe1393c91acd6b1163cf1a"]/div[2]/p[1]')
    loc_调查问卷 = (By.XPATH, '//li[@id="5cfe12f1c91acd6b1163cf18"]/div[2]/p[1]')

    def click_科普专题(self):
        self.mouse_over_click(self.loc_科普专题)

    def click_咨询公告(self):
        self.mouse_over_click(self.loc_咨询公告)

    def click_健康知识(self):
        self.mouse_over_click(self.loc_健康知识)

    def click_圈子论坛(self):
        self.mouse_over_click(self.loc_圈子论坛)

    def click_健康科普(self):
        self.mouse_over_click(self.loc_健康科普)

    def click_应用市场(self):
        self.click_element(self.loc_应用市场)
        return self

    def click_医生课堂(self):
        self.mouse_over_click(self.loc_医生课堂)
        return self

    def click_我的应用(self):
        self.mouse_over_click(self.loc_我的应用)
        return self

    def click_医院推荐(self):
        self.mouse_over_click(self.loc_医院推荐)
        return self

    def click_调查问卷(self):
        self.mouse_over_click(self.loc_调查问卷)
        return self
