from pymongo import MongoClient
from common.config import  ReadConfig
# 1,建立连接：数据库的连接信息：
# 2,新建一个查询页面
# 3， 编写SQL
# 4，执行SQL
# 5，查看结果
# 6，关闭查询
# 7，关闭数据库连接
class Do_mongo:
   def __init__(self):
       host = ReadConfig().get('setsql','host')
       # user = ReadConfig().get('setsql','user')
       # password = ReadConfig().get('setsql','password')
       #database = ReadConfig().get('setsql','database')
       port = ReadConfig().get_int('setsql', 'port')
       client=MongoClient(host,port)
       db=client.test
       collection = db.test
       collection.insert({"title": "test"})
       for item in collection.find():
           print(item)



   def fetch_one(self,sql): #获取只有一行的数据
       self.cursor.execute(sql)#查询sql
       self.mysql.commit()
       return self.cursor.fetchone()#获取数据

   def fetch_all(self,sql):#获取所有行的数据
       self.cursor.execute(sql)
       self.mysql.commit()
       return self.cursor.fetchall()

   def close(self):
       self.cursor.close()
       self.mysql.close()

if __name__ == '__main__':
    r=Do_mysql()
    s=r.fetch_one("SELECT * FROM db_koala.t_doctor b where b.ClinicUniqueID in ( select userid from db_flybear.t_user u where u.dentalid='60616' and u.roleid=2 ) and name ='小李'")
    print(s)
    r.close()




