#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author  : Andy
# @time    : 2019/2/28 17:12
# @File    : fetchall.py
# @Software: k3/cloud

import pymysql

db =pymysql.connect('120.79.86.225','demo','123.com','stock_sfabric20190225')

cursor=db.cursor()

tables =['yarn_stock_in', 'dye_stock_in', 'printing_stock_in', 'knit_stock_in', 'yarn_stock_out', 'dye_stock_out',
          'printing_stock_out',
          'knit_stock_out', 'knit_stock_in_detail_history', 'yarn_stock_out_detail_history']

for t in tables:
    try:
        sql='update'+ t + 'set is_success=0'
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
