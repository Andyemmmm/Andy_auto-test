from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Science_mangement(SeleniumBase):
    '''
    这个是社区--应用模块--科普专题--专题管理页面
    '''
    loc_专题管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[1]')
    loc_专题文章管理 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[2]')
    loc_专题邀约管理 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[3]')
    loc_专题分类管理 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[4]')
    loc_新建专题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_邀约医生写专题 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div/div[2]/div/a[1]/button/span')
    loc_选取文章拼凑专题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div/div[2]/div/a[2]/button')
    loc_取消弹窗 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div/div[1]/button')
    loc_专题状态_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[1]')
    loc_专题状态_已发布 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[2]')
    loc_专题状态_已下线 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[3]')
    loc_专题状态_待发布 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[4]')
    loc_专题科室_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[1]')
    loc_专题科室_皮肤科 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[2]')
    loc_专题科室_皮肤病 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[3]')
    loc_专题科室_儿科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[4]')
    loc_专题科室_妇产科 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[5]')
    loc_专题科室_皮肤性病科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[6]')
    loc_专题科室_内科 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[7]')
    loc_专题科室_外科 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[8]')
    loc_专题分类_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li[1]')
    loc_专题分类_健康专题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li[2]')
    loc_邀约创建日期_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[1]')

    loc_邀约创建日期_今日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[2]')
    lco_邀约创建日期_昨日 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[3]')
    loc_邀约创建日期_本周 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[4]')
    loc_邀约创建日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[5]')
    loc_专题发布日期_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[1]')
    loc_专题发布日期_今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[2]')
    loc_专题发布日期_昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[3]')
    loc_专题发布日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[4]')
    loc_专题发布日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[5]')
    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')
    loc_专题邀约新建成功 = (By.XPATH, '/html/body/div[2]/p')
    loc_列表第一行 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
    loc_第一行发布 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[15]/div/button/span')
    loc_发布确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    def click_专题管理(self):
        self.click_element(self.loc_专题管理)
        return self

    def click_专题文章管理(self):
        self.click_element(self.loc_专题文章管理)
        return self

    def click_专题邀约管理(self):
        self.click_element(self.loc_专题邀约管理)

    def click_专题分类管理(self):
        self.click_element(self.loc_专题分类管理)

    def click_新建专题(self):
        self.click_element(self.loc_新建专题)
        return self

    def click_邀约医生写专题(self):
        self.mouse_over_click(self.loc_邀约医生写专题)
        return self

    def click_选取文章拼凑专题(self):
        self.click_element(self.loc_选取文章拼凑专题)
        return self

    def click_取消弹窗(self):
        self.click_element(self.loc_取消弹窗)
        return self

    def click_专题状态全部(self):
        self.click_element(self.loc_专题状态_全部)

    def click_专题专题已发布(self):
        self.click_element(self.loc_专题状态_已发布)

    def click_专题状态已下线(self):
        self.click_element(self.loc_专题状态_已下线)

    def click_专题状态待发布(self):
        self.click_element(self.loc_专题状态_待发布)
        return self

    def click_专题科室全部(self):
        self.click_element(self.loc_专题科室_全部)

    def click_专题科室皮肤科(self):
        self.click_element(self.loc_专题科室_皮肤科)

    def click_专题科室皮肤病(self):
        self.click_element(self.loc_专题科室_皮肤病)

    def click_专题科室儿科(self):
        self.click_element(self.loc_专题科室_儿科)

    def click_专题科室妇产科(self):
        self.click_element(self.loc_专题科室_妇产科)

    def click_专题科室皮肤性病科(self):
        self.click_element(self.loc_专题科室_皮肤性病科)

    def click_专题科室内科(self):
        self.click_element(self.loc_专题科室_内科)

    def click_专题科室外科(self):
        self.click_element(self.loc_专题科室_外科)

    def click_专题分类全部(self):
        self.click_element(self.loc_专题分类_全部)

    def click_专题分类健康专题(self):
        self.click_element(self.loc_专题分类_健康专题)

    def click_邀约创建日期全部(self):
        self.click_element(self.loc_邀约创建日期_全部)

    def click_邀约创建日期今日(self):
        self.click_element(self.loc_邀约创建日期_今日)

    def click_邀约创建日期昨日(self):
        self.click_element(self.lco_邀约创建日期_昨日)

    def click_邀约创建日期本周(self):
        self.click_element(self.loc_邀约创建日期_本周)

    def click_邀约创建日期本月(self):
        self.click_element(self.loc_邀约创建日期_本月)

    def click_专题发布日期全部(self):
        self.click_element(self.loc_专题发布日期_全部)

    def click_专题发布日期今日(self):
        self.click_element(self.loc_专题发布日期_今日)

    def click_专题发布日期昨日(self):
        self.click_element(self.loc_专题发布日期_昨日)

    def click_专题发布日期本周(self):
        self.click_element(self.loc_专题发布日期_本周)

    def click_专题发布日期本月(self):
        self.click_element(self.loc_专题发布日期_本月)

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)

    def get_专题邀约新建成功(self):
        return self.get_element_text(self.loc_专题邀约新建成功)

    def get_获取列表第一行(self):
        return self.get_element_text(self.loc_列表第一行)

    def click_第一行发布(self):
        self.click_element(self.loc_第一行发布)
        return self

    def click_发布确定(self):
        self.click_element(self.loc_发布确定)
