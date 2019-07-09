import unittest
from loan_project.common.api_request import Api_request
from ddt import ddt,data,unpack
from loan_project.common.Excel_data import Do_Excel
import json
from loan_project.common.domysql import Do_mysql
from loan_project.common import context
from loan_project.common.config import ReadConfig
from loan_project.common import contants
from loan_project.common import loging
logger=loging.Log(__name__)
@ddt
class TestCaesinvest(unittest.TestCase):
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
    def test_invest(self,case):
        logger.info('开始测试:{}'.format(case.title))
    #先替换掉cases表中的变量
        case.data = context.replace(case.data)
        #然后发送登录请求,
        #根据请求的手机号在数据库查到memberID
        if case.sql is not None:
            sql = eval(case.sql)  # 将str转换成字典



    #将memberID传给loan_member_id, 请求接口
    #根据标的名称和创建时间去查到最新的标的loan_id,传给loan_id,发送请求
    #登录投资人账号,根据请求的手机号在数据库查到memberID和密码,

        res=self.http_request.http_request(method=case.method,url=case.url,data=case.data)
        #查询数据库有没有该用户
        try:
            self.assertEqual(str(case.expected),res.json()['code'])
            self.excel.write_excel(row=case.case_id + 1, actual=res.text,result='PASS')
            if res.json()['msg'] == "加标成功":
                loan_id = Do_mysql().fetch_one(sql['sql1'])
                setattr(context.Context, 'loan_id', loan_id['id'])

                # 保存到类属性里面
            if 'mobilephone' in case.data:
                if eval(case.data)['mobilephone'] == ReadConfig().get('data', 'mobilephone'):
                    sql = context.replace(sql['sql1'])
                    normal_member_id = Do_mysql().fetch_one(sql)['id']
                    setattr(context.Context, 'normal_member_id', normal_member_id)
                    setattr(context.Context, 'normal_pwd', '123456')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id+1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

