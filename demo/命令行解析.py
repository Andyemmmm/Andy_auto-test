import argparse

# 创建解析
parser = argparse.ArgumentParser(
    description="命令行解析 Demo"  # 用来说明这个程序在做什么
)

# 添加参数
# parser.add_argument("pos1", help="位置参数1")
# parser.add_argument(
#     "-o", "--option-age",
#     help="可选参数",
#     dest="opt",
#     default="默认值"
# )
# 必写属性，第一位
parser.add_argument("name", type=str, help="姓名")
# 必写属性，第二位
parser.add_argument("birth", type=str, help="生日")
# 可选属性，默认 None
parser.add_argument("-r", "--race", type=str, dest="race", help="民族")
# 可选属性，范围限制
parser.add_argument("-a", "--age", type=int, dest="age", help="年龄", default=0, choices=range(150))
# 可选属性，范围
parser.add_argument("-s", "--sex", type=str, dest="sex", help="性别", required=True, default="男", choices=["男", "女"])
# 多个参数
parser.add_argument("-o", "--other", type=str, dest="other", help="其他信息", nargs="*")
# 布尔参数
parser.add_argument("-b", dest="bachelordom", action="store_true", help="单身 ")

# 解析参数
args = parser.parse_args()
print(args)
# print(args.race)

# python 命令行解析.py
# python 命令行解析.py 李四
# python 命令行解析.py 李四 20
# python 命令行解析.py 李四 20 -r 汉族
# python 命令行解析.py 李四 20 -r 汉族 -a 50
# python 命令行解析.py 李四 20 -r 汉族 -a 50 -s 女
# python 命令行解析.py 李四 20 -r 汉族 -a 50 -s 女 -o A B C D
# python 命令行解析.py 李四 20 -r 汉族 -a 50 -s 女 -o A B C D -b
