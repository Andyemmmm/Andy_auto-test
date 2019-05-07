card_infor = []#全局变量
def print_menu():
    #1 打印功能区域
    print ("="*50)
    print (" 名片管理系统v1.0版")
    print ("1、添加一个新的名字")
    print ("2、删除一个名字")
    print ("3、修改一个名字")
    print ("4、查询一个名字")
    print ("5、显示所有的信息")
    print ("6、退出系统")
    print ("="*50)

def add_card_infor():
    '''添加一个新的名字功能'''
    new_name =input ("请输入一个新的名字：")
    new_qq = input ("请输入一个QQ：")
    new_weixin = input ("请输入一个微信：")
    new_addr = input("请输入一个地址：")
    #定义一个空的字典
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["qq"] = new_qq
    new_infor["weixin"] = new_addr
    #将字典放到列表中
    global card_infor#修改全局变量
    card_infor.append(new_infor)
    print(card_infor)

def select_name():
    '''查询名字的功能'''
    global card_infor
    find_name = input("请输入一个要查找的名字：")
    find_flag = 0 #默认表示没有找到
    for exam in card_infor:
        if find_name == exam["name"]:
            print ("找到此人了")
            find_flag = 1 #表示找到了
            break
    #判断是否找到了
        if find_flag == 0:
            print ("查无此人")
def print_card_infor():
    '''打印名字列表'''
    global card_infor
    print ("姓名\tQQ\t微信\t住址")
    for temp in card_infor:
     print(temp)

def main():
    '''完成对整个程序的控制'''
    #调用打印功能的函数
    print_menu()

    while True:
        #2 获取用户输入
        num = input("请输入操作序号：")
        num =int(num)
        #3 根据用户输入执行对应的程序
        if num == 1:
         add_card_infor()
        elif num == 2:
         pass
        elif num == 3:
         pass
        elif num == 4:
         select_name()
        elif num == 5:
         print_card_infor()
        elif num == 6:
         break
        else:
         print ("输入有误，请重新输入")
        print ("")#隔开一行
#调用主函数
main()