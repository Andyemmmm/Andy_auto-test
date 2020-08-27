from configparser import ConfigParser

# 实例化
config = ConfigParser()
# 读取配置文件
config.read("demo/test.ini", encoding='utf-8')

# 读取内容
print(config["browser"]["name"])
print(config.get("browser", "name"))
print(config.getboolean("local", "local_browser"))
print(config.getint("local", "wait_time"))
print(config.getfloat("local", "wait_time"))

# 修改配置文件：先读取，再写入
config.set("browser", "name", "firefox")

# 添加新的块
config.add_section("user")
config.set("user", "id", "001")

with open("demo/test.ini", 'w', encoding='utf-8') as f:
    config.write(f)  # 将数据写入配置文件
