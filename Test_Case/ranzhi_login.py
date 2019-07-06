import unittest
import requests
import re
from HTMLReport import logger

from Business.url import url_test
from Common.md5 import get_md5


class Ranzhi_login(unittest.TestCase):
    def setUp(self):
        self.s = requests.Session()
        logger().info("初始化 session")
        pass

    def tearDown(self):
        self.s.close()
        logger().info("关闭 session")
        pass

    def test_login(self):
        account = "admin"
        password = "admin123"
        logger().info("打开登录页获取随机值")
        s = self.s

        querystring = {"m": "user", "f": "login"}
        logger().info(f"params：{querystring}")
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        }
        logger().info(f"headers：{headers}")
        r = s.get(url_test + "/ranzhi/www/sys/index.php", headers=headers, params=querystring)
        logger().info(f"status_code：{r.status_code}")
        logger().info(f"url：{r.url}")
        logger().info(f"url：{r.headers}")
        logger().info(f"cookies：{r.cookies.items()}")
        logger().info(f"text：{r.text}")
        random = re.search(r'v.random = "(.*?)";', r.text).group(1)
        logger().info(f"random：{random}")

        logger().info("登录请求")
        pwd1 = get_md5(password)
        logger().info(f"第一次加密：{pwd1}")
        pwd2 = get_md5(pwd1 + account)
        logger().info(f"第二次加密：{pwd2}")
        pwd3 = get_md5(pwd2 + random)
        logger().info(f"第三次加密：{pwd3}")

        headers_login = headers.copy()
        headers_login.update({
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded",
            "Connection": "keep-alive",
            "X-Requested-With": "XMLHttpRequest",
        })
        data = {
            "account": account,
            "password": pwd3,
            "referer": "",
            "rawPassword": pwd1,
            "keepLogin": False
        }
        logger().info(f"params：{querystring}")
        logger().info(f"headers_login：{headers_login}")
        logger().info(f"data：{data}")
        r = s.post(
            url_test + "/ranzhi/www/sys/index.php",
            headers=headers_login,
            params=querystring,
            data=data
        )
        logger().info(f"status_code：{r.status_code}")
        logger().info(f"url：{r.url}")
        logger().info(f"url：{r.headers}")
        logger().info(f"cookies：{r.cookies.items()}")
        logger().info(f"text：{r.text}")

        self.assertEqual(200, r.status_code)
        self.assertEqual("success", r.json().get("result"))
        self.assertIn("locate", r.json())
        pass
