from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Doctor(SeleniumBase):
    '''这个是社区--医生模块页面'''
    loc_标签管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/span')
    loc_邀请医生 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/a/button')
    loc_医生列表第一行名称 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/button/span')

    # loc_首页 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[1]/li/span')
    # loc_社区 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[2]/li/span')
    # loc_医生 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[3]/li/span')
    # loc_用户 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[4]/li/span')
    # loc_财务 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[5]/li/span')
    # loc_应用 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[6]/li/span')
    # loc_设置 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[7]/li/span')

    def click_标签管理(self):
        self.click_element(self.loc_标签管理)
        return self

    def mouse_click_邀请医生(self):
        self.mouse_over_click(self.loc_邀请医生)
        return self

    def get_邀请成功(self):
        return self.get_element_text(self.loc_医生列表第一行名称)


class Page_Label_Management(SeleniumBase):
    '''这个是社区---医生模块--标签管理的页面'''
    loc_新建标签 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button')
    loc_第一行编辑按钮 = (By.XPATH, '//div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/button[1]')
    loc_第一行删除按钮 = (By.XPATH, '//div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/button[2]')
    loc_新建标签输入框 = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/input')
    loc_新建标签确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')
    loc_新建标签取消 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
    loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    def click_新建标签(self):
        self.click_element(self.loc_新建标签)
        return self

    def click_编辑(self):
        self.click_element(self.loc_第一行编辑按钮)
        return self

    def click_删除(self):
        self.click_element(self.loc_第一行删除按钮)
        return self

    def send_标签(self, name):
        self.send_keys(self.loc_新建标签输入框, name)
        return self

    def click_确定(self):
        self.click_element(self.loc_新建标签确定)
        return self

    def click_取消(self):
        self.click_element(self.loc_新建标签取消)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)
