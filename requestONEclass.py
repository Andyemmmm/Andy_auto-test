# coding:utf8


import requests
url="http://www.baidu.com"
z=requests.get(url)
print(z.status_code)

print(z.url)
print(z.text)