#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author  : Andy
# @time    : 2019/2/28 15:06
# @File    : 小雨.py
# @Software: k3/cloud

import pymysql

# 打开数据库连接
db = pymysql.connect("120.79.86.225", "demo", "123.com", "stock_sfabric20190225")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()