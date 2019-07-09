import unittest
from common.api_request import Api_request
from ddt import ddt,data,unpack
from common.Excel_data import Do_Excel
import json
from common.domysql import Do_mysql
from common.loging import Log
from common import contants
logger = Log(__name__)
@ddt
class TestCaesregister(unittest.TestCase):
    excel = Do_Excel(contants.case_file, 'register')
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
    def test_request_register(self,case):
        #首先判断这个值是不是变量
        logger.info('开始测试:{}'.format(case.title))
        case.data = eval(case.data)  #转换表格读出来的数据
        if case.sql is not None:
            case.sql = eval(case.sql)
            if case.data["mobile"] == 'mobilephone':
                    max_phone = Do_mysql().fetch_one(case.sql["sql1"])["MAX(mobilephone)"]
                    max_phone = int(max_phone) -52354 #这里写个随便电话号码
                    print(max_phone)
                    case.data["mobilephone"] = max_phone

        res=self.http_request.http_request(method=case.method,url=case.url,data=case.data)
        #查询数据库有没有该用户
        try:
            self.assertEqual(case.expected,res.text)
            if case.sql is not None:
                sql = case.sql["sql2"] + str(max_phone)
                member = Do_mysql().fetch_one(sql)
                after =member['mobilephone']
                self.assertEqual(after, case.data["mobilephone"])
            self.excel.write_excel(row=case.case_id + 1, actual=res.text,result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id+1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

