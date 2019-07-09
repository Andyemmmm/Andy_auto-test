import unittest
from common.api_request import Api_request
from ddt import ddt,data
from common.Excel_data import Do_Excel
from common.domysql import Do_mysql
from common import context
from common import contants
from common import loging
from common import randomname
import json
logger=loging.Log(__name__)
@ddt
class TestCaespatsplitsub(unittest.TestCase):
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
    def test_patsplitsub(self,case):
        logger.info('开始测试:{}'.format(case.title))
        case.data =context.replace(case.data)
        res=self.http_request.http_request(method=case.method,url=case.url,data=case.data)
        print(res.request)
        try:
            self.assertEqual(str(case.expected),res.json()['info'])
            if case.title == '登录成功':
               setattr(context.Context,'patientname',randomname.random_name())
               # print(context.Context.patientname)
            if case.title == '新建患者成功':
                # sql = eval(context.replace(case.sql))
                doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
                setattr(context.Context,'doctorid',doctorid)
                setattr(context.Context, 'customerid', res.json()['list']['customerid'])
            self.excel.write_excel(row=case.case_id + 1,actual=res.text,result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1,actual=res.text,result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))


