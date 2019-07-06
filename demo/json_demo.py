# http://json.org/json-zh.html
"""
序列化：encoding，把Python对象编码转化成json字符串
反序列化：decoding，把json格式字符串解码转换为Python对象
"""
import json

data = [{"name": "李四", "leng": ("python", "c"), 'age': 40, "man": False}]
data_json = json.dumps(data, ensure_ascii=False)
print(data_json)
data_json = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2)
print(data_json)

new_data = json.loads(data_json)

# 写入文件
with open("demo/text.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open("demo/text.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    print(j)
    print(type(j))
