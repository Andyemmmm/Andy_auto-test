#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author  : Andy
# @time    : 2019/2/28 15:06
# @File    : 小雨.py
# @Software: k3/cloud

# import pymysql
# #
# # # 打开数据库连接
# # db = pymysql.connect("120.79.86.225", "demo", "123.com", "stock_sfabric20190225")
# #
# # # 使用 cursor() 方法创建一个游标对象 cursor
# # cursor = db.cursor()
# #
# # # 使用 execute() 方法执行 SQL，如果表存在则删除
# # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# #
# # # 使用预处理语句创建表
# # sql = """CREATE TABLE EMPLOYEE (
# #          FIRST_NAME  CHAR(20) NOT NULL,
# #          LAST_NAME  CHAR(20),
# #          AGE INT,
# #          SEX CHAR(1),
# #          INCOME FLOAT )"""
# #
# # cursor.execute(sql)
# #
# # # 关闭数据库连接
# # db.close

# 1.分别使用for、while循环，去除列表[1, 4, 3, 4, 3, 4, 1, 2, 6]中的数字4
# 1.用for循环实现
# local=[1,4,3,4,3,4,1,2,6]
# print(f'没有删除前的列表：{local}')
# l=len(local)
# for _ in range(l):
#     if 4 not in local:
#         break
#     local.remove(4)
# print(f'删除后的列表：{local}')
# 2.用while循环实现
lc=[1,4,3,4,3,4,1,2,6]
print(f'原来的列表：{lc}')
le=len(lc)
i=0
while i<le:
    if 4 not in lc:
        break
    lc.remove(4)
    i += 1
print(f'修改之后的列表：{lc}')

# for i in range(1, 10):  # 输出行
#     for j in range(1, i + 1):  # 输出 行中内容
#         print(f"{j} * {i} = {i * j}", end="\t")
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()
