import pymysql
from Common.tools.rw_ini import read_config


# 1,建立连接：数据库的连接信息：
# 2,新建一个查询页面
# 3， 编写SQL
# 4，执行SQL
# 5，查看结果
# 6，关闭查询
# 7，关闭数据库连接
class Do_mysql:
    def __init__(self):
        rc = read_config("Config/env.ini")
        host = rc.get('mysql', 'host')
        user = rc.get('mysql', 'user')
        password = rc.get('mysql', 'password')
        # database = rc.get('mysql','database')
        port = rc.getint('mysql', 'port')
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self, sql):  # 获取只有一行的数据
        self.cursor.execute(sql)  # 查询sql
        self.mysql.commit()
        return self.cursor.fetchone()  # 获取数据

    def fetch_all(self, sql):  # 获取所有行的数据
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    r = Do_mysql()
    s = r.fetch_one(
        "SELECT * from wenwo.t_basic_datadanalysis_data_point_20_05_26 where channel_id='test_love120200526' ORDER BY id desc")
    print(s)
    r.close()
