#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/26 16:19
# @File     : page_new_community.py
# @Software : aiwen_ui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase
import time


class Page_New_community(SeleniumBase):
    '''这个是社区B端---新建社区页面'''
    loc_医院诊所 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[1]')
    loc_其他机构 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[2]')
    loc_医生团队 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[3]')
    loc_项目型社区 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[4]')
    loc_测试社区 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[5]')
    loc_测试社区_医院 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[5]/div/ul/li[1]')
    loc_测试社区_机构集团 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[5]/div/ul/li[2]')
    loc_测试社区_医生团队 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[5]/div/ul/li[3]')
    loc_测试社区_项目型 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/li[5]/div/ul/li[4]')
    loc_上一步 = (By.XPATH, '//*[@id="app"]/div/div[3]/button[1]/span')
    loc_下一步 = (By.XPATH, '//*[@id="app"]/div/div[3]/button[2]/span')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_社区(self, type):
        if type == '医院':
            self.click_element(self.loc_医院诊所)
        elif type == '机构':
            self.click_element(self.loc_其他机构)
        elif type == '医生团队':
            self.click_element(self.loc_医生团队)
        elif type == '项目型社区':
            self.click_element(self.loc_项目型社区)
        else:
            print('社区类型输入有误，请重新输入！')
        return self

    def click_测试社区(self, type):
        if type == '医院':
            self.click_element(self.loc_测试社区_医院)
        elif type == '机构':
            self.click_element(self.loc_测试社区_机构集团)
        elif type == '医生团队':
            self.click_element(self.loc_测试社区_医生团队)
        elif type == '项目型社区':
            self.click_element(self.loc_测试社区_项目型)
        else:
            print('测试社区类型输入有误，请重试！')
        return self

    def click_pre(self):
        self.click_element(self.loc_上一步)
        return self

    def click_next(self):
        self.click_element(self.loc_下一步)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)


class Page_community_info(SeleniumBase):
    '''新建社区下一步---社区信息页签'''
    loc_名称 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/input')
    loc_Slogan = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/input')
    loc_简称 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/input')
    loc_简介 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/textarea')
    loc_logo = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/div[1]/input')
    loc_logo_确定 = (By.XPATH, '//div[@aria-label="裁剪图片"]//button[2]/span[text()="确 定"]')
    loc_特色科室 = (By.XPATH, '//form/div[6]/div/div[1]/div/input')
    loc_擅长疾病 = (By.XPATH, '//form/div[7]/div/div[1]/div/input')

    def send_名称(self, name):
        self.send_keys(self.loc_名称, name)
        return self

    def send_Slogan(self, slogan):
        self.send_keys(self.loc_Slogan, slogan)
        return self

    def send_简称(self, abbreviation):
        self.send_keys(self.loc_简称, abbreviation)
        return self

    def send_简介(self, brief):
        self.send_keys(self.loc_简介, brief)
        return self

    def send_logo(self, png):
        self.send_png(self.loc_logo, png)
        return self

    def click_logo_确定(self):
        self.click_element(self.loc_logo_确定)
        return self

    def click_特色科室(self, option):
        self.send_keys(self.loc_特色科室, option)
        try:
            ele = self.driver.find_element_by_xpath(
                f"//ul/li[normalize-space(text())='{option}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            try:
                self.driver.find_element_by_xpath(
                    '//div[@class="el-autocomplete-suggestion__wrap el-scrollbar__wrap"]/ul/li[1]').click()
            except:
                self.send_keys(self.loc_特色科室, '内科')
                ele = self.driver.find_element_by_xpath("//ul/li[normalize-space(text())='内科']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        return self

    def click_擅长疾病(self, option):
        self.send_keys(self.loc_擅长疾病, option)
        try:
            ele = self.driver.find_element_by_xpath(
                f"//ul/li[normalize-space(text())='{option}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            try:
                self.driver.find_element_by_xpath(
                    '//div[@class="el-autocomplete-suggestion__wrap el-scrollbar__wrap"]/ul/li[1]').click()
            except:
                self.send_keys(self.loc_擅长疾病, '冠心病')
                ele = self.driver.find_element_by_xpath(
                    "//ul/li[normalize-space(text())='冠心病']")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        return self


'''新建医院社区的页面'''


class Page_Hospital(SeleniumBase):
    '''新建---医院社区的页面'''
    loc_hospital_name = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[1]/div/div/div[1]/input')
    loc_hospital_addr = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[2]/div/div/input')
    loc_addr = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/input')
    loc_addr_option = (By.XPATH, '//ol/li[1]')
    loc_addr_confirm = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/div/div/div[3]/span/button[2]/span')
    loc_经营性质 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[3]/div/div/div/input')
    loc_经营性质_公立 = (By.XPATH, "//span[text()='公立']")
    loc_经营性质_私立 = (By.XPATH, "//span[text()='私立']")
    loc_医院类型 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[4]/div/div/div[1]/input')
    loc_医院类型_医院 = (By.XPATH, "//span[text()='医院']")
    loc_医院类型_诊所 = (By.XPATH, "//span[text()='诊所']")
    loc_医院类型_社区卫生服务中心 = (By.XPATH, "//span[text()='社区卫生服务中心']")
    loc_医院类型_卫生所 = (By.XPATH, "//span[text()='卫生所']")

    def send_hoapital_name(self, name):
        self.send_keys(self.loc_hospital_name, name)
        return self

    def send_hospital_addr(self, addr):
        self.click_element(self.loc_hospital_addr)
        time.sleep(0.5)
        self.send_keys(self.loc_addr, addr)
        time.sleep(5)
        try:
            self.mouse_over_click(self.loc_addr_option)
        except:
            time.sleep(1)
            self.mouse_over_click(self.loc_addr_option)
        self.click_element(self.loc_addr_confirm)
        return self

    def click_经营性质(self, option):
        self.click_element(self.loc_经营性质)
        if option == '公立':
            self.mouse_over_click(self.loc_经营性质_公立)
        elif option == '私立':
            self.mouse_over_click(self.loc_经营性质_私立)
        else:
            print('参数输入有误，请重试！')

        return self

    def click_医院类型(self, option):
        self.ex_script(self.loc_医院类型)
        self.click_element(self.loc_医院类型)
        if option == '医院':
            self.mouse_over_click(self.loc_医院类型_医院)
        elif option == '诊所':
            self.mouse_over_click(self.loc_医院类型_诊所)
        elif option == '社区卫生服务中心':
            self.mouse_over_click(self.loc_医院类型_社区卫生服务中心)
        elif option == '卫生所':
            self.mouse_over_click(self.loc_医院类型_卫生所)
        else:
            print('参数输入有误，请重试！')

        return self


class Page_certificated_information_hospital(SeleniumBase):
    '''新建---医院的认证资料页面'''
    loc_沿用上一个社区资料 = (By.XPATH, '//form/div[1]/div/label/span[1]/span')
    loc_企业名称 = (By.XPATH, '//form/div[2]/div/div/input')
    loc_营业执照 = (By.XPATH, '//form/div[3]/div/div/div[1]/div/div[1]/input')
    loc_执业许可证 = (By.XPATH, '//form/div[4]/div/div/div[1]/div/div[1]/input')
    loc_其他证件 = (By.XPATH, '//form/div[5]/div/div/div[1]/div/div[1]/input')
    loc_联系人 = (By.XPATH, '//form/div[6]/div/div/input')
    loc_联系方式 = (By.XPATH, '//form/div[7]/div/div/input')

    def click_沿用上一个社区资料(self):
        self.click_element(self.loc_沿用上一个社区资料)
        return self

    def send_企业名称(self, name):
        self.send_keys(self.loc_企业名称, name)
        return self

    def send_营业执照(self, png):
        self.send_png(self.loc_营业执照, png)
        return self

    def send_执业许可证(self, png):
        self.send_png(self.loc_执业许可证, png)
        return self

    def send_其他证件(self, png):
        self.send_png(self.loc_其他证件, png)
        return self

    def send_联系人(self, name):
        self.send_keys(self.loc_联系人, name)
        return self

    def send_联系方式(self, phone):
        self.send_keys(self.loc_联系方式, phone)
        return self


'''新建机构社区的页面'''


class Page_organization(SeleniumBase):
    '''新建---机构社区的页面'''
    loc_集团机构名称 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[1]/div/div[1]/input')
    loc_集团机构地址 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/form/div[2]/div/div/input')
    loc_send_addr = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/input')
    loc_addr_option = (By.XPATH, '//ol/li[1]')
    loc_addr_confirm = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[4]/div/div/div/div[3]/span/button[2]/span')

    def send_集团机构名称(self, name):
        self.send_keys(self.loc_集团机构名称, name)
        return self

    def send_集团机构地址(self, addr):
        self.ex_script(self.loc_集团机构地址)
        self.click_element(self.loc_集团机构地址)
        time.sleep(0.5)
        self.send_keys(self.loc_send_addr, addr)
        time.sleep(4)
        self.mouse_over_click(self.loc_addr_option)
        self.click_element(self.loc_addr_confirm)
        return self


class Page_certificated_information_organization(SeleniumBase):
    '''新建社区---机构集团的认证资料页面'''
    loc_企业名称 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/form/div[1]/div/div/input')
    loc_营业执照 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div/div[1]/input')
    loc_其他证件 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/form/div[3]/div/div/div[1]/div/div[1]/input')
    loc_联系人 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/form/div[4]/div/div/input')
    loc_联系方式 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/form/div[5]/div/div/input')

    def send_企业名称(self, name):
        self.send_keys(self.loc_企业名称, name)
        return self

    def send_营业执照(self, png):
        self.send_png(self.loc_营业执照, png)
        return self

    def send_其他证件(self, png):
        self.send_png(self.loc_其他证件, png)
        return self

    def send_联系人(self, name):
        self.send_keys(self.loc_联系人, name)
        return self

    def send_联系方式(self, phone):
        self.send_keys(self.loc_联系方式, phone)
        return self


'''新建医生团队社区的页面'''


class Page_Doctor_team(SeleniumBase):
    '''新建---医生团队社区的页面'''
    loc_非爱问平台医生 = (By.XPATH, "//span[text()='非爱问平台医生']")
    loc_爱问平台医生 = (By.XPATH, "//span[text()='爱问平台医生']")
    loc_add = (By.XPATH, "//ul[@class='doctor-list']/div")
    loc_doctor_mz = (By.XPATH, "//input[@placeholder='请输入医生名字']")
    loc_确定 = (By.XPATH, '//div[4]/div/div[2]/div/div[@class="el-dialog__footer"]/span/button[2]')
    loc_doctor_name = (By.XPATH, "//input[@placeholder='请输入医生姓名']")
    loc_doctor_head = (By.XPATH, "//div[@class='relation-box']//input[@type='file']")
    loc_doctor_head_确定 = (By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]/span')
    loc_doctor_裁切1 = (By.XPATH, '/html/body/div[7]/div/div[3]/span/button[2]/span')
    loc_职称 = (By.XPATH, "//div[@class='relation-box']//input[@placeholder='请选择职称']")
    loc_执业医院 = (By.XPATH, "//div[@class='relation-box']//input[@placeholder='请输入医生执业医院']")
    loc_添加医生确定 = (By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[4]/div/div[2]/div/div[3]//span[text()='确 定']")

    def click_非爱问平台医生(self):

        self.mouse_over_click(self.loc_非爱问平台医生)
        return self

    def click_爱问平台医生(self):
        self.mouse_over_click(self.loc_爱问平台医生)
        return self

    def click_add(self):
        self.ex_script(self.loc_add)
        self.mouse_over_click(self.loc_add)
        return self

    def send_doctor_mz(self, name):
        self.send_keys(self.loc_doctor_mz, name)
        try:
            ele = self.driver.find_element_by_xpath(
                f"//div[@class='el-scrollbar']//li[contains(text(),'{name}')]")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            try:
                self.driver.find_element_by_xpath("//div[@class='el-scrollbar']//li[1]").click()
            except:
                self.send_keys(self.loc_doctor_mz, '大陆zqh')
                ele = self.driver.find_element_by_xpath(f"//div[@class='el-scrollbar']//li[contains(text(),'大陆zqh')]")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        return self

    def click_确定(self):
        self.click_element(self.loc_确定)
        return self

    def send_doctor_name(self, name):
        self.send_keys(self.loc_doctor_name, name)
        return self

    def send_doctor_head(self, png):
        self.send_png(self.loc_doctor_head, png)
        return self

    def click_裁切(self):
        self.click_element(self.loc_doctor_head_确定)
        return self

    def click_裁切1(self):
        self.click_element(self.loc_doctor_裁切1)
        return self

    def click_职称(self, job):
        self.click_element(self.loc_职称)
        try:
            ele = self.driver.find_element_by_xpath(
                f"//div[@class='el-select-dropdown el-popper']//span[text()='{job}']")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            ele = self.driver.find_element_by_xpath("//div[@class='el-select-dropdown el-popper']//li[1]/span")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        return self

    def send_执业医院(self, hospital):
        self.send_keys(self.loc_执业医院, hospital)
        return self

    def click_添加医生确定(self):
        self.click_element(self.loc_添加医生确定)
        return self


class Page_certificated_information_doctor(SeleniumBase):
    '''新建社区---医生团队认证资料页面'''
    loc_承诺函 = (By.XPATH, '//input')
    loc_上传资质1 = (By.XPATH, '//ul[@class="doctor-list iwen-doc-list"]/li[1]/div[2]/div')
    loc_上传资质2 = (By.XPATH, '//ul[@class="doctor-list iwen-doc-list"]/li[2]/div[2]/div')
    loc_上传资质3 = (By.XPATH, '//ul[@class="doctor-list iwen-doc-list"]/li[3]/div[2]/div')
    loc_身份证正面 = (By.XPATH, '//div[@class="mb20"]/div/div[1]/div/div/div/div/input')
    loc_身份证反面 = (By.XPATH, '//div[@class="mb20"]/div/div[2]/div/div/div/div/input')
    loc_执业证 = (By.XPATH, '//div[@class="mb20"]/following-sibling::div//input')
    loc_上传资质确定 = (By.XPATH, '//div[@class="el-dialog__body"]/following-sibling::div/span/button[2]/span')

    def send_承诺函(self, png):
        self.send_png(self.loc_承诺函, png)
        return self

    def click_上传资质1(self):
        self.click_element(self.loc_上传资质1)
        return self

    def click_上传资质2(self):
        self.click_element(self.loc_上传资质2)
        return self

    def click_上传资质3(self):
        self.click_element(self.loc_上传资质3)
        return self

    def send_资质(self, id_card_front, id_card_reverse, practice):
        self.send_keys(self.loc_身份证正面, id_card_front)
        self.send_keys(self.loc_身份证反面, id_card_reverse)
        self.send_keys(self.loc_执业证, practice)
        time.sleep(3)
        self.click_element(self.loc_上传资质确定)
        return self


'''新建项目型社区的页面'''


class Page_Project_community(SeleniumBase):
    '''新建---项目型社区的页面'''
    loc_项目名称 = (By.XPATH, '//div[4]/div/form/div[1]/div/div[1]/input')
    loc_项目介绍 = (By.XPATH, '//div[4]/div/form/div[2]/div/div/textarea')

    def send_项目名称(self, name):
        self.send_keys(self.loc_项目名称, name)
        return self

    def send_项目介绍(self, introduce):
        self.send_keys(self.loc_项目介绍, introduce)
        return self


class Page_success(SeleniumBase):
    '''新建---社区创建成功页面'''
    loc_msg = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/h2')
    loc_community_name = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[1]/div/h4')
    loc_community_status = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[1]/span')

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_status(self):
        return self.get_element_text(self.loc_community_status)

    def get_community_name(self):
        return self.get_element_text(self.loc_community_name)
