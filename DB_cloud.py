# coding:utf-8
import pymysql
import time
import pymysql

# 打开数据库
db = pymysql.connect(host='120.79.86.225', port=3306, user='demo', passwd='123.com', db='uat_sfabric1213',
                     charset="utf8")
# print db
cursor = db.cursor()
# 查询语句
# sql_select = "select version()"
# cursor.execute(sql_select)
# data = cursor.fetchone()
# print("DB version is : %s" % data)
# (更新表的列（is_success=0）)
tables = ['yarn_stock_in', 'dye_stock_in', 'printing_stock_in', 'knit_stock_in', 'yarn_stock_out', 'dye_stock_out',
          'printing_stock_out',
          'knit_stock_out', 'knit_stock_in_detail_history', 'yarn_stock_out_detail_history']
# tables = ['dye_stock_out', 'knit_stock_out']
for t in tables:
    try:
        sql = 'update ' + t + ' set is_success=0'
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()