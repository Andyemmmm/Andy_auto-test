from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Health_science(SeleniumBase):
    '''这个是健康科普--科普管理文章页面'''
    loc_科普管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[1]')
    loc_科普邀约管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[2]')
    loc_科普筛选 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[3]')
    loc_科普分类管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[4]')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/div/input')
    loc_搜索框按钮 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/div/div/button')
    loc_新建文章邀约 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/a/button/span')
    loc_科普类型_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]')
    loc_科普类型_文章 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[2]')
    loc_科普类型_视频 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]')
    loc_所属科室_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]')
    loc_所属科室_皮肤科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[2]')
    loc_所属科室_皮肤病 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[3]')
    loc_所属科室_儿科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[4]')
    loc_所属科室_妇产科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[5]')
    loc_所属科室_皮肤性病科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[6]')
    loc_所属科室_内科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[7]')
    loc_所属科室_外科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[8]')
    loc_所属科室_五官科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[9]')
    loc_所属科室_口腔科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[10]')
    loc_所属科室_中医科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[11]')
    loc_所属科室_传染科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[12]')
    loc_所属科室_精神心理科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[13]')
    loc_所属科室_肿瘤科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[14]')
    loc_所属科室_麻醉医学科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[15]')
    loc_标签_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/ul/li')
    loc_分类_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[4]/ul/li[1]')
    loc_分类_健康科普 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[4]/ul/li[2]')
    loc_分类_诊间日记 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[4]/ul/li[3]')
    loc_分类_病例分析 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[4]/ul/li[4]')
    loc_来源_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[1]')
    loc_来源_文章邀约 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[2]')
    loc_来源_医生诊室 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[3]')
    loc_来源_专题邀约 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[4]')
    loc_来源_其它 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[5]')
    loc_发布日期_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[6]/ul/li[1]')
    loc_发布日期_今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[6]/ul/li[2]')
    loc_发布日期_昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[6]/ul/li[3]')
    loc_发布日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[6]/ul/li[4]')
    loc_发布日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[6]/ul/li[5]')
    loc_清空筛选条件按钮 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/button/span')
    loc_发布成功 = (By.XPATH, '//div[2]/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')

    def get_发布成功(self):
        return self.get_element_text(self.loc_发布成功)

    def send_搜索框(self, keyword):
        self.send_keys(self.loc_搜索框, keyword)
        return self

    def click_搜索框按钮(self):
        return self.click_element(self.loc_搜索框按钮)

    def click_科普管理(self):
        self.click_element(self.loc_科普管理)

    def click_科普邀约管理(self):
        self.click_element(self.loc_科普邀约管理)

    def click_科普筛选(self):
        self.click_element(self.loc_科普筛选)

    def click_科普分类管理(self):
        self.click_element(self.loc_科普分类管理)

    def click_新建文章邀约(self):
        self.mouse_over_click(self.loc_新建文章邀约)

    def click_科普类型_全部(self):
        self.click_element(self.loc_科普类型_全部)

    def click_科普类型_文章(self):
        self.click_element(self.loc_科普类型_文章)

    def click_科普类型_视频(self):
        self.click_element(self.loc_科普类型_视频)

    def click_所属科室_全部(self):
        self.click_element(self.loc_所属科室_全部)

    def click_所属科室_皮肤科(self):
        self.click_element(self.loc_所属科室_皮肤科)

    def click_所属科室_皮肤病(self):
        self.click_element(self.loc_所属科室_皮肤病)

    def click_所属科室_儿科(self):
        self.click_element(self.loc_所属科室_儿科)

    def click_所属科室_妇产科(self):
        self.click_element(self.loc_所属科室_妇产科)

    def click_所属科室_皮肤性病科(self):
        self.click_element(self.loc_所属科室_皮肤性病科)

    def click_所属科室_内科(self):
        self.click_element(self.loc_所属科室_内科)

    def click_所属科室_外科(self):
        self.click_element(self.loc_所属科室_外科)

    def click_所属科室_五官科(self):
        self.click_element(self.loc_所属科室_五官科)

    def click_所属科室_口腔科(self):
        self.click_element(self.loc_所属科室_口腔科)

    def click_所属科室_中医科(self):
        self.click_element(self.loc_所属科室_中医科)

    def click_所属科室_传染科(self):
        self.click_element(self.loc_所属科室_传染科)

    def click_所属科室_精神心理科(self):
        self.click_element(self.loc_所属科室_精神心理科)

    def click_所属科室_肿瘤科(self):
        self.click_element(self.loc_所属科室_肿瘤科)

    def click_所属科室_麻醉医学科(self):
        self.click_element(self.loc_所属科室_麻醉医学科)

    def click_标签_全部(self):
        self.click_element(self.loc_标签_全部)

    def click_分类_全部(self):
        self.click_element(self.loc_分类_全部)

    def click_分类_健康科普(self):
        self.click_element(self.loc_分类_健康科普)

    def click_分类_诊间日记(self):
        self.click_element(self.loc_分类_诊间日记)

    def click_分类_病例分析(self):
        self.click_element(self.loc_分类_病例分析)

    def click_来源_全部(self):
        self.click_element(self.loc_来源_全部)

    def click_来源_文章邀约(self):
        self.click_element(self.loc_来源_文章邀约)

    def click_来源_医生诊室(self):
        self.click_element(self.loc_来源_医生诊室)

    def click_来源_专题邀约(self):
        self.click_element(self.loc_来源_专题邀约)

    def click_来源_其它(self):
        self.click_element(self.loc_来源_其它)

    def click_发布日期_全部(self):
        self.click_element(self.loc_发布日期_全部)

    def click_发布日期_今日(self):
        self.click_element(self.loc_发布日期_今日)

    def click_发布日期_昨日(self):
        self.click_element(self.loc_发布日期_昨日)

    def click_发布日期_本周(self):
        self.click_element(self.loc_发布日期_本周)

    def click_发布日期_本月(self):
        self.click_element(self.loc_发布日期_本月)

    def click_清空筛选条件按钮(self):
        return self.click_element(self.loc_清空筛选条件按钮)
