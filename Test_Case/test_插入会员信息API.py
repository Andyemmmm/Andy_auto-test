import json
import unittest
import requests
import random
from HTMLReport import logger

from Business.key import app_key
from Business.url import url_test_dsc_api
from Common.md5 import get_md5


class Test_插入会员信息API(unittest.TestCase):
    def setUp(self):
        logger().info("初始化 session")
        self.session = requests.Session()
        pass

    def tearDown(self):
        logger().info("关闭 session")
        self.session.close()
        pass

    def test_插入会员信息API(self):
        session = self.session
        n = 11
        user_name = f"liu3{n}"
        password = "123456"
        mobile_phone = f"133112211{n}"
        email = user_name + "@qq.com"
        ec_salt = random.randint(100, 999)

        logger().info(f"原始密码:{password}")
        pwd1 = get_md5(password)
        logger().info(f"加密密码_1:{pwd1}")
        pwd2 = get_md5(f"{pwd1}{ec_salt}")
        logger().info(f"加密密码_2:{pwd2}")

        params = {
            "method": "dsc.user.insert.post",
            "app_key": app_key,
            "format": "json"
        }
        data = {
            "data": json.dumps(
                {
                    'email': email,
                    'user_name': user_name,
                    'mobile_phone': mobile_phone,
                    'password': pwd2,
                    'ec_salt': ec_salt
                }
            )
        }

        respose = session.post(url_test_dsc_api + "", params=params, data=data)
        logger().info(respose.status_code)
        logger().info(respose.url)
        logger().info(respose.text)
        logger().info(respose.json())

        self.assertEqual(200, respose.status_code)
        self.assertEqual("success", respose.json().get("result"))
        self.assertEqual(0, respose.json().get("error"))
        self.assertEqual("数据提交成功", respose.json().get("msg"))
        self.assertIn("info", respose.json())
        self.assertEqual(email, respose.json().get("info").get("email"))
        self.assertEqual(user_name, respose.json().get("info").get("user_name"))
        self.assertEqual(mobile_phone, respose.json().get("info").get("mobile_phone"))
        self.assertEqual(pwd2, respose.json().get("info").get("password"))
        self.assertEqual(ec_salt, respose.json().get("info").get("ec_salt"))
        self.assertIn("user_id", respose.json().get("info"))
        pass
