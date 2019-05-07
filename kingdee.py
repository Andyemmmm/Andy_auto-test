import requests
import json
from config import Config
from db import Db
import time


class kingdee(object):
    def __init__(self):
        self.config = Config.config()
        self.session = requests.Session()
        db = Db()
        self.cursor = db.cursor
        self.conn = db.conn

    def login(self):
        '''
        登录金蝶云系统
        :return:
        '''
        url = self.config['base']['url'] + 'Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc'
        params = {'acctID': self.config['base']['account'],
                  'username': self.config['base']['username'],
                  'password': self.config['base']['password'],
                  'lcid': self.config['base']['lang']
                  }
        res = self.session.post(url, params)
        result = json.loads(res.text.encode('utf8'))
        if result['LoginResultType'] == 1:
            print('success')
            pass
        else:
            print('failure')
            pass

    def save(self, data):
        '''
        保存单据到金蝶云
        :param data:
        :return:
        '''
        url = self.config['base']['url'] + 'Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Save.common.kdsvc'
        res = self.session.post(url, data)
        result = json.loads(res.text.encode('utf8'))
        return result

    def submit(self, data):
        '''
        提交金蝶云里面的单据
        :param data:
        :return:
        '''
        url = self.config['base']['url'] + 'Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Submit.common.kdsvc'
        res = self.session.post(url, data)
        result = json.loads(res.text.encode('utf8'))
        return result

    def audit(self, data):
        '''
        审核金蝶云里面的单据
        :param data:
        :return:
        '''
        url = self.config['base']['url'] + 'Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Audit.common.kdsvc'
        res = self.session.post(url, data)
        result = json.loads(res.text.encode('utf8'))
        return result

    def view(self, data):
        '''
        查看金蝶云里面的单据
        :param data:
        :return:
        '''
        url = self.config['base']['url'] + 'Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.View.common.kdsvc'
        res = self.session.post(url, data)
        result = json.loads(res.text.encode('utf8'))
        return result

    def saveLog(self, data, result='', item=''):
        '''
        记录本次单据同步的日志
        :param data:
        :param result:
        :param item:
        :return:
        '''
        if result['Result']['ResponseStatus']['IsSuccess'] == 1:
            data['is_success'] = 1
            bool = True
        else:
            data['is_success'] = 0
            error = result['Result']['ResponseStatus']['Errors'][0]['Message']
            errors = []
            for e in error:
                msg = '字段名称：'.e['FieldName'] + ' 错误信息：' + e['Message']
                errors.append(msg)
            data['reason'] = '【' + item + '】' + ';'.join(errors)
            bool = False
        data['created'] = int(time.time())
        sql = 'insert into kingdee_log(code,created,transmission_time,is_success,reason) values("%s","%d","%s","%s","%s")' % (
            data['code'], data['created'], data['transmission_time'], data['is_success'], data['reason'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        return bool

    def transmit(self):
        '''
        传递各种单据到金蝶云中
        :return:
        '''
        pass


if __name__ == '__main__':
    k = kingdee()
    k.login()