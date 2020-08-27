from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Invitation_topic(SeleniumBase):
    '''
    这个是社区--应用模块--科普专题--专题管理--新建邀约专题页面
    '''

    loc_邀约名称 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[1]/div[1]/div/div[1]/input')
    loc_邀约简介 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[1]/div[3]/div/div[1]/textarea')
    loc_有效时间 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[1]/div[4]/div/div/input[1]')
    loc_开始日期 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[1]/span[1]/div/input')
    loc_开始时间 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input')
    loc_开始时间确定 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[1]/span[2]/div[2]/div[2]/button[2]')
    loc_结束日期 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[3]/span[1]/div/input')
    loc_结束时间 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input')
    loc_结束时间确定 = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[3]/span[2]/div[2]/div[2]/button[2]')
    loc_有效时间确定 = (By.XPATH, '/html/body/div[2]/div[2]/button[2]/span')
    loc_专题名称 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[1]/div/div[1]/input')
    loc_专题介绍 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[2]/div/div[1]/textarea')
    loc_专题封面 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[3]/div/div[1]/div/div/input')
    loc_一级科室 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[4]/div/div[1]/div/input')

    loc_二级科室 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[4]/div/div[2]/div[1]/input')

    loc_专题分类 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[5]/div/div/div[1]/input')
    loc_专题分类_选项 = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')
    loc_新增分类 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[5]/div/button/span')
    loc_输入分类名称 = (By.XPATH, '/html/body/div[6]/div/div[2]/div[2]/div[1]/input')
    loc_输入分类名称确定 = (By.XPATH, '/html/body/div[6]/div/div[3]/button[2]/span')

    loc_是原创 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[6]/div/label[1]/span[1]')
    lco_否原创 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[6]/div/label[2]/span[1]/span')
    loc_选择科室_急诊科 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[8]/div/div/div/label[1]/span[1]/span')
    loc_全选科室 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[2]/div[8]/div/div/label/span[1]/span')
    loc_每篇奖励 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[3]/div[1]/div/div/input')
    loc_要求数量 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/form[3]/div[2]/div/div/input')
    loc_提交 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/button[1]/span')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/button[2]')
    loc_金币数 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/span')
    loc_金币不足提示 = (By.XPATH, '/html/body/div[6]/p')

    def send_邀约名称(self, name):
        self.send_keys(self.loc_邀约名称, name)
        return self

    def send_邀约简介(self, about):
        self.send_keys(self.loc_邀约简介, about)
        return self

    def click_有效时间(self):
        self.click_element(self.loc_有效时间)
        return self

    def send_开始日期(self, start_date):
        self.send_keys(self.loc_开始日期, start_date)
        return self

    def send_开始时间(self, start_time):
        self.send_keys(self.loc_开始时间, start_time)
        return self

    def click_开始时间确定(self):
        self.click_element(self.loc_开始时间确定)
        return self

    def send_结束日期(self, end_date):
        self.send_keys(self.loc_结束日期, end_date)
        return self

    def send_结束时间(self, end_time):
        self.send_keys(self.loc_结束时间, end_time)
        return self

    def click_结束时间确定(self):
        self.click_element(self.loc_结束时间确定)
        return self

    def click_有效时间确定(self):
        self.click_element(self.loc_有效时间确定)
        return self

    def send_专题名称(self, nickname):
        self.send_keys(self.loc_专题名称, nickname)
        return self

    def send_专题介绍(self, niabout):
        self.send_keys(self.loc_专题介绍, niabout)
        return self

    def send_专题封面(self, png):
        self.send_png(self.loc_专题封面, png)
        return self

    def click_一级科室(self):
        self.click_element(self.loc_一级科室)
        return self

    def mouse_一级科室_科室(self, value):
        if value == '妇产科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '儿科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '皮肤性病科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '内科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '外科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '五官科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '口腔科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '中医科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '传染科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '精神心理科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '肿瘤科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '麻醉医学科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '急诊科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '药剂科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '营养科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '男科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '生殖健康科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '康复医学科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '整形美容科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '介入医学科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '职业病科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '医学影像科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '病理科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '其它':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        if value == '全科':
            ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        else:
            print('你给的一级科室参数错误')

        return self

    def click_二级科室(self):
        self.click_element(self.loc_二级科室)
        return self

    def click_二级科室_科室(self, value):
        try:
            if value == '小儿内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '小儿外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '产科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '妇科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '皮肤病':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '皮肤科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '性病科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '内分泌科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '呼吸内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '心血管内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '消化内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '神经内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '肾内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '血液科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '风湿科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '普内科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '烧伤整形科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '心胸外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '泌尿外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '普外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '肝胆外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '神经外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '血管外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '乳腺外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '肛肠外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '骨外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '脊柱外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '手足外科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '眼科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '耳鼻喉科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '结核病科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '传染病其他科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '麻醉科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '疼痛科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '整形美容科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '烧伤整形':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            if value == '超声科':
                ele = self.driver.find_element_by_xpath(f"//span[text()='{value}']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            else:
                print('你给的二级科室参数错误')
        except:
            self.click_element(self.loc_二级科室)

        return self

    def click_是原创(self):
        self.click_element(self.loc_是原创)
        return self

    def click_否原创(self):
        self.click_element(self.lco_否原创)
        return self

    def click_选择科室_急诊科(self):
        self.click_element(self.loc_选择科室_急诊科)
        return self

    def click_全选科室(self):
        self.click_element(self.loc_全选科室)
        return self

    def send_每篇奖励(self, num):
        self.send_keys(self.loc_每篇奖励, num)
        return self

    def send_要求数量(self, number):
        self.send_keys(self.loc_要求数量, number)
        return self

    def click_提交(self):
        self.click_element(self.loc_提交)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def get_金币数(self):
        return self.get_element_text(self.loc_金币数)

    def get_金币数不足提示(self):
        return self.get_element_text(self.loc_金币不足提示)

    def click_专题分类(self):
        self.click_element(self.loc_专题分类)
        return self

    def click_专题分类_选项(self):
        self.mouse_over_click(self.loc_专题分类_选项)
        return self
