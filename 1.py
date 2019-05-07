import pymysql

class Check():
    #类的初始化
    def __init__(self):
        self.host='120.79.86.225'
        self.port='3306'
        self.user='demo'
        self.passwd='123.com'
        self.db='stock_sfabric20190225'


    #连接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset="utf8")
            self.cursor = self.conn.cursor()
            self.conut =self.cursor.execute("SELECT VERSION()")
            self.data =self.conut.fetchone()
            print("Database version : %s " % self.data)



        except:
            print("connect mysql error")

Check()