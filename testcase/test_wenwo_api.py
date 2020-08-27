#!/usr/bin/python3

# @Author   : Andy
# @time     : ${DATE} ${TIME}
# @File     : ${NAME}.py
# @Software : ${PROJECT_NAME}

import unittest
import requests
from common.api_request import Api_request
from ddt import ddt, data
from common.Excel_data import Do_Excel
from common.domysql import Do_mysql
from common import context
from common import contants
from common import loging
from common.split_str import spl
from requests_toolbelt.multipart.encoder import MultipartEncoder
from common import randomname
import json

logger = loging.Log(__name__)


@ddt
class TestCasewenwo(unittest.TestCase):
    '''这是一个【注册，登陆】机构管理的接口测试类'''
    excel = Do_Excel(contants.case_file, 'invest')
    case = excel.read_Excel()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = Api_request()

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

    @data(*case)
    def test_001(self, case):
        '''【注册，登陆】机构管理的接口测试'''
        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replace(case.data)
        if case.title == '个人中心-绑定新手机号' or case.title == '修改密码' or case.title == '更新个人资料':
            token = getattr(context.Context, 'token')
            header = {"token": str(token)}
            print(header)
            res = self.http_request.http_request(method=case.method, url=case.url, data=case.data, headers=header)

        else:
            res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])
            if case.title == '登陆':
                setattr(context.Context, 'token', res.json()['data']['token'])

            if case.title == '首页-工作台':
                pass
            # setattr(context.Context,'patientname',randomname.random_name())
            # print(context.Context.patientname)
            # if case.title == '新建患者成功':
            #     # sql = eval(context.replace(case.sql))
            #     doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
            #     setattr(context.Context,'doctorid',doctorid)
            #     setattr(context.Context, 'customerid', res.json()['list']['customerid'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

    """
    # code is far away from bugs with the god animal protecting
        I love animals. They taste delicious.
              
    """


@ddt
class Testpatsplitsub(unittest.TestCase):
    '''分类管理-添加B端官网用户信息的测试类'''
    excel = Do_Excel(contants.case_file, 'patsplitsub')
    case = excel.read_Excel()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = Api_request()

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

    @data(*case)
    def test_001(self, case):
        '''分类管理-添加B端官网用户信息'''
        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replace(case.data)

        res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])
            # if case.title == '登陆':
            #     setattr(context.Context, 'token', res.json()['data']['token'])
            #
            # if case.title == '首页-工作台':
            #     pass
            # setattr(context.Context,'patientname',randomname.random_name())
            # print(context.Context.patientname)
            # if case.title == '新建患者成功':
            #     # sql = eval(context.replace(case.sql))
            #     doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
            #     setattr(context.Context,'doctorid',doctorid)
            #     setattr(context.Context, 'customerid', res.json()['list']['customerid'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

        """
            # code is far away from bugs with the god animal protecting
                I love animals. They taste delicious.
             
            """


@ddt
class TestdoctorClass(unittest.TestCase):
    '''医生课堂视频的测试类'''
    excel = Do_Excel(contants.case_file, 'doctorclass')
    case = excel.read_Excel()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = Api_request()

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

    @data(*case)
    def test_001(self, case):
        '''医生视频课堂的测试用例'''
        url = 'https://b.991kang.com//api/video/upload'
        url1 = 'https://b.991kang.com//api/videoInvite/importInviteDoctor'
        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replace(case.data)
        if case.title == '视频分片上传':
            da, headers = spl(case.data)
            headers = {'Content-Type': headers}
            res = requests.post(url, data=da, headers=headers)

        elif case.title == '导入邀请的医生数据':
            da, headers = spl(case.data)
            headers = {'Content-Type': headers}
            print(da, headers)
            res = requests.post(url1, data=da, headers=headers)

        else:
            res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])
            # if case.title == '登陆':
            #     setattr(context.Context, 'token', res.json()['data']['token'])
            #
            # if case.title == '首页-工作台':
            #     pass
            # setattr(context.Context,'patientname',randomname.random_name())
            # print(context.Context.patientname)
            # if case.title == '新建患者成功':
            #     # sql = eval(context.replace(case.sql))
            #     doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
            #     setattr(context.Context,'doctorid',doctorid)
            #     setattr(context.Context, 'customerid', res.json()['list']['customerid'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

        """
            # code is far away from bugs with the god animal protecting
                I love animals. They taste delicious.
               
            """


@ddt
class Data_other(unittest.TestCase):
    '''数据其它的测试类'''
    excel = Do_Excel(contants.case_file, 'data_other')
    case = excel.read_Excel()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = Api_request()

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

    @data(*case)
    def test_001(self, case):
        '''数据统计--文件上传--新闻管理--活动邀请产出内容'''
        url = 'https://b.991kang.com//api/article/synchronizeData'
        url1 = 'https://b.991kang.com//api/file/uploadFile'
        url2 = 'https://b.991kang.com//api/file/uploadFiles'
        url3 = 'https://b.991kang.com//api/file/uploadImg'
        url4 = 'https://b.991kang.com//api/statistics/synchronizeData'
        url5 = 'https://b.991kang.com//api/community/getMyCommunitys'

        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replace(case.data)
        if case.title == '同步健康科普打点数据':
            headers = {
                'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjgwOTM3MzA2NDIsInBheWxvYWQiOiJcIjE1MzIzNzUxMjgwXCIifQ.cyStrI3VrjvM-QmWrMmByYmHjXIMvYTRDxBeZ9Td0P4'}
            res = requests.post(url, headers=headers)
        elif case.title == '同步健康科普打点数据1':
            headers = {
                'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjgwOTM3MzA2NDIsInBheWxvYWQiOiJcIjE1MzIzNzUxMjgwXCIifQ.cyStrI3VrjvM-QmWrMmByYmHjXIMvYTRDxBeZ9Td0P4'}
            res = requests.post(url4, headers=headers)
        elif case.title == '我的社区列表':
            headers = {
                'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjgwOTM3MzA2NDIsInBheWxvYWQiOiJcIjE1MzIzNzUxMjgwXCIifQ.cyStrI3VrjvM-QmWrMmByYmHjXIMvYTRDxBeZ9Td0P4'}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.get(url5, data=data, headers=headers)
        elif case.title == '单文件上传':
            da, headers = spl(case.data)
            headers = {'Content-Type': headers}
            res = requests.post(url1, data=da, headers=headers)

        elif case.title == '多文件上传':
            da, headers = spl(case.data)
            headers = {'Content-Type': headers}
            res = requests.post(url2, data=da, headers=headers)

        elif case.title == '图片上传':
            da, headers = spl(case.data)
            headers = {'Content-Type': headers}
            res = requests.post(url3, data=da, headers=headers)

        else:
            res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])
            # if case.title == '登陆':
            #     setattr(context.Context, 'token', res.json()['data']['token'])
            #
            # if case.title == '首页-工作台':
            #     pass
            # setattr(context.Context,'patientname',randomname.random_name())
            # print(context.Context.patientname)
            # if case.title == '新建患者成功':
            #     # sql = eval(context.replace(case.sql))
            #     doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
            #     setattr(context.Context,'doctorid',doctorid)
            #     setattr(context.Context, 'customerid', res.json()['list']['customerid'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

        """
            # code is far away from bugs with the god animal protecting
                I love animals. They taste delicious.
               
            """


if __name__ == '__main__':
    unittest.main()
