#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 10:29
# @File     : read_txt.py
# @Software : Test_dental

def read_txt(file):
    '''
    :param file: 文件路径
    :return:
    '''
    L=[]
    with open(file,'r',encoding='utf-8')as f:
        for line in f:
            #去除换行符
            if line[-1]=='\n':
                line=line[:-1]
            #去除空行
            if line=='':
                continue
            #去除注释
            if line[0]=='#':
                continue
            L.append(line.split('|'))  #按|拆分追加到列表中
    return L

if __name__=='__main__':
    L=read_txt('../data/预约埋点点击次数.txt')
    print(L)