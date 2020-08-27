from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Questionnaire_download(SeleniumBase):
    '''
    这个是应用市场里面的调查问卷模块开通页面
    '''

    loc_调查问卷 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[2]/p[1]')
    loc_开通 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[3]/button')
    loc_确定开通 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    def get_获取调查问卷文本(self):
        return self.get_element_text(self.loc_调查问卷)

    def click_开通(self):
        self.click_element(self.loc_开通)
        return self

    def click_确定开通(self):
        self.click_element(self.loc_确定开通)
        return self
