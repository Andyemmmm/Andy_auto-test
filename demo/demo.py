#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/19 10:43
# @File     : demo.py
# @Software : Test_dental

# class num:
#     def sum(self,n):
#         return sum(range(1,n+1))
# if __name__=="__main__":
#     scp=num()
#     s=scp.sum(100)
#     print(s)

# list=[7,6,3,8,9,1,2,5]
# newlist=[]
# def get_min(list):
#     a=min(list)
#     list.remove(a)
#     newlist.append(a)
#     if len(list)>0:
#         get_min(list)
#     return newlist
# newlist=get_min(list)
# print(newlist)
#  九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()
#  字典排序
# d={'d1':1,'d2':2,'d3':6,'d4':5}
# s=sorted(d.items(),key=lambda x:x[1],reverse=False)
# print(s)
#  递归求和
# def get_sum(num):
#     if num>=1:
#         res=num+get_sum(num-1)
#     else:
#         res=0
#     return res
# res=get_sum(100)
# print(res)
#  1加到n的和
# def sm(n):
#     a=0
#     b=1
#     for i in range(1,n):
#         a=a+b
#         b+=1
#     print(a)
# sm(101)
import requests
import json
from common.split_str import spl

# url='https://b.991kang.com/api/bcustomer/login'
# url='https://b.991kang.com//api/bcustomer/regsiter'
# url='https://b.991kang.com//api/bcustomer/updateBindPhone'
# url = 'https://b.991kang.com//api/bcustomer/h5PhoneLogin'
# url='https://b.991kang.com//api/bcustomer/resetPwd'
# url='https://b.991kang.com/api/bcustomer/checkCode'
#
# data='"dataJson":{"phone":"18679610587","code":"666666","sourceType":"H5"}'
# data=spl(data)
# print(type(data))
# print(data)
# a = {
#     'dataJson': json.dumps(
#         {
#             'phone': '13058157849',
#             'code': '666666',
#             'sourceType':'H5'
#
#         }
#     )
# }
# print(type(a))
# print(f'a的参数是{a}')


import os
import time
import zipfile
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from common.split_str import spl

# header = {
#     'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzYxNTU3MzgzNDksInBheWxvYWQiOiJcIjE4Njc5NjEwNTg3XCIifQ.leV0kTgeVhODFGuK5xdWzqtiCkCxggr3lzy56bCTceo'}
#
#

url = 'https://b.991kang.com//api/file/uploadImg'
# url1 = 'http://192.168.255.223:52128//api/doctor/live/getAllLiveList'
# da={"file_id": "test01",
#             "id": "10001",
#             "paraMap":"1",
#             "slice_cnt":"0",
#             "slice_md5":"0",
#             "slice_no":"1",
#             "slice_bin": ('test01.xlsx', open(r'C:\Users\Doctor\Desktop\tutu\111.png', 'rb'),
#                      'application/octet-stream')}
#
data={'file': ('test01.xlsx', open(r'C:\Users\Doctor\Downloads\doctor.xlsx', 'rb'),
                     'application/octet-stream')}

# print(type(data))
#
m = MultipartEncoder(fields=data)
#
# # m ,c= spl(a)
# print(m)
# print(type(m))
#
headers={
    'Content-Type':m.content_type
}
# data={
#     "ids": "1"
# }
# data = {"page":"1","size":"10","userId":"1"}
# data = {'roomId':1,'userId':1}
# data = {'id':'1','likeNum':'100'}
# data="dataJson={'phone':'18679610587','password':'123456'}	"
# data1 = {'page': '1', 'size': '10', 'id': '1'}
# data = json.dumps(data)
# data=json.loads(data)
# print(type(data))
# headers = {'Content-Type': 'application/json '}


res = requests.post(url, data=m, headers=headers)
# res1 = requests.get(url1, params=data1)
print(res.json())
print(res.url)
