import unittest
import requests
from HTMLReport import logger
from config.url import Host


class Test_Bplatfrom_adduser(unittest.TestCase):
    '''
    此类为测试B端官网添加用户信息
    '''

    def setUp(self):
        logger().info('测试开始,初始化一个session')
        self.session = requests.session()

    def tearDown(self):
        logger().info('测试结束，关闭会话')
        self.session.close()

    def test_Bplatfrom_adduser(self):
        session = self.session
        headers = {
            'consumes': 'application/json',
            'produces': 'application/json;charset=UTF-8'
        }

        data = {
            'dataJson': "{'name':'陈真1','phone':'12345678','company':'火山5'}"
        }

        respose = session.post(Host + '/api/customerinfo/add', headers=headers, data=data)
        logger().info(f'状态码：', respose.status_code)
        logger().info(f'url：', respose.url)
        logger().info(f'返回结果：', respose.text)
        logger().info(f'返回结果：', respose.json())

        self.assertEqual(200, respose.status_code)
        self.assertEqual(200, respose.json().get('status'))

    def test_tail(self):
        session = self.session
        data = {
            'dataJson': "{'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMwOTY0MTU3NjYsInBheWxvYWQiOiJcInRpbmFcIiJ9.0XfJu_aZOgVuelKCyIq3R8NWl0KjKXvedSKM5R-ZgUs','page':'1','size':'100'}"
        }
        respose = session.get(Host + '/api/customerinfo/pageCustomerInfo', data=data)
        logger().info(f'状态码：', respose.status_code)
        logger().info(f'url：', respose.url)
        logger().info(f'返回结果：', respose.text)
        logger().info(f'返回结果：', respose.json())

        self.assertEqual(200, respose.status_code)
        self.assertEqual(200, respose.json().get('status'))
        self.assertEqual('成功', respose.json().get('message'))
