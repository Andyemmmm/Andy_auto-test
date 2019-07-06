# https://2.python-requests.org//zh_CN/latest/
import requests

url = "http://192.168.2.252:81/"

r = requests.request("GET", url + "/get")
print(r.status_code)
print(r.headers)
print(r.headers.get("Date"))
print(r.encoding)
print(r.text)
print(r.json())

params_payload = {"a": 1, "b": 2, "c": [1, 2]}
r = requests.request("GET", url + "/get", params=params_payload)
print(r.url)
data_payload = {"a": 11, "b": 22, "c": [11, 22]}
r = requests.request("POST", url + "/post", data=data_payload)
print(r.text)
json_payload = {"a": 111, "b": 222, "c": [111, 222]}
r = requests.request("POST", url + "/post", json=json_payload)
print(r.text)
r = requests.request("POST", url + "/post", json=json_payload, params=params_payload)
print(r.text)

headers = {"User-Agent": "MyAPP/1.5.0"}
r = requests.request("GET", url + "/get", headers=headers)
print(r.text)

cookies = {"name": "lisi"}
r = requests.request("GET", url + "/cookies", cookies=cookies)
print(r.text)

files = {"file": open("demo/test.xml", 'rb')}
r = requests.request("post", url + "/post", files=files)
print(r.text)

# 鉴权
r = requests.request(
    "GET",
    url + "/basic-auth/user/passwd",
    auth=("user", "passwd")
)
print(r.text)

requests.request("get", url + "/delay/6", timeout=5)
requests.request("get", url + "/delay/6", timeout=(1, 7))
requests.request("get", url + "/delay/6", timeout=None)
requests.request("get", "https://www.google.com")

proxies = {
    "http": "http://192.168.64.1:10800",
    "https": "http://192.168.64.1:10800",
    # "https://www.google.com": "http://user:pass@192.168.64.1:10800"
}
r = requests.request(
    "get",
    "https://www.google.com/",
    proxies=proxies
)
print(r.status_code)
print(r.text)

r = requests.request("get", url + "/redirect/6")
print(r.status_code)
print(r.history[1].url)
print(r.history[3].url)
print(r.url)
r = requests.request("get", url + "/redirect/6", allow_redirects=False)
print(r.status_code)
print(r.url)
print(r.history)

requests.request("get", url, verify=False)
requests.request("get", "https://www.baidu.com", verify=False)
requests.request(
    "get",
    "https://www.baidu.com",
    cert=("*.crt", "*.key")
)

from contextlib import closing

with closing(requests.request("get", url + "/stream/5", stream=True)) as r:
    # for c in r.iter_content(10):
    #     print(c)
    for c in r.iter_lines(1):
        print(c)

# requests.get()
# requests.post()
# requests.delete()

r1 = requests.get(url + "/cookies/set", params={"a": "1"})
r2 = requests.get(url + "/cookies")
print(r1.text)
print(r2.text)

s = requests.Session()
# s.request(url=url,params=)
r3 = s.get(url + "/cookies/set", params={"a": "1"})
r4 = s.get(url + "/cookies")
print(r3.text)
print(r4.text)
s.close()
