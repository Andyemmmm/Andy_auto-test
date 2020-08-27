#!/usr/bin/python3
# @Author   : Andy
# @time     : 2019/12/2 14:31
# @File     : test_online_class.py
# @Software : Test_dental

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
class TestdoctorClass(unittest.TestCase):
    ''' 在线直播V4.6版本的测试类'''
    excel = Do_Excel(contants.case_file, 'online_class')
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
        '''在线直播V4.6版本的测试用例'''
        url = 'http://192.168.255.223:52128/api/doctor/live/createLive'
        url1 = 'http://192.168.255.223:52128//api/doctor/live/updateLiveInfo'
        url2 = 'http://192.168.255.223:52128/api/doctor/live/updateStatus'
        url3 = 'http://192.168.255.223:52128//api/doctor/participation/addParticipateRecord'
        url4 = 'http://192.168.255.223:52128//api/doctor/participation/getUserCountByLiveIds'
        url5='http://192.168.255.223:52128//api/doctor/participation/saveRecordList'
        url6='http://192.168.255.223:52128//api/doctor/liveComment/getCommentCountByLiveIds'
        url7='http://192.168.255.223:52128//api/doctor/liveComment/sendMessage'
        url8='http://192.168.255.223:52128//api/doctor/card/editLiveTab'
        url9='http://192.168.255.223:52128//api/doctor/channel/createChannel'
        url10='http://192.168.255.223:52128//api/doctor/channel/updateChannel'
        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replace(case.data)
        if case.title == '创建直播课程':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url, data=data, headers=headers)

        elif case.title == '更新直播课程信息':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url1, data=data, headers=headers)

        elif case.title == '修改直播课程状态':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url2, data=data, headers=headers)

        elif case.title == '添加参与报名记录,主要用于邀请主讲医生':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url3, data=data, headers=headers)

        elif case.title == '通过直播课程ids批量获取课程报名人数':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url4, data=data, headers=headers)

        elif case.title == '批量添加参与报名记录,主要用于邀请观看医生':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url5, data=data, headers=headers)

        elif case.title == '通过直播课程ids批量获取课程评论数':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url6, data=data, headers=headers)

        elif case.title == '评论或回复评论':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url7, data=data, headers=headers)

        elif case.title == '编辑页签':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url8, data=data, headers=headers)

        elif case.title == '创建直播频道':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url9, data=data, headers=headers)

        elif case.title == '修改直播频道信息':
            headers = {'Content-Type': 'application/json '}
            da = eval(case.data)
            data = json.dumps(da)
            res = requests.post(url10, data=data, headers=headers)
        else:
            res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))



if __name__ == '__main__':
    unittest.main()
