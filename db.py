# coding=utf-8
import os
import sys

import pymysql

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from config import Config


class Db(object):
    '''
    如果有指定，则使用指定的数据库连接，否则默认根据配置文件中base模块设置的db来连接数据库
    '''

    def __init__(self, db=None):
        config = Config.config()
        if db is None:
            config = config['db']
        else:
            config = config[db]
        self.conn = pymysql.connect(host=config['host'], user=config['username'],
                                    password=config['password'], port=int(config['port']),
                                    database=config['database'],
                                    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()
