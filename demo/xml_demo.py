# http://www.w3school.com.cn/xml/index.asp
from xml.etree import ElementTree as ET

# 建立一个xml解析树对象
tree = ET.ElementTree(file="demo/test.xml")
tree1 = ET.fromstring(
    """<bookstore>
<book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
</book>
<book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
</book>
<book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
</book>
</bookstore>"""
)

# 获得根
root = tree.getroot()
print(root.tag)
root.attrib

# 读孩子节点
for child in root:
    print(child.tag, child.attrib)

# 直接读取
root[0].tag
root[0].attrib
root[0].text

root[0][0].tag
root[0][0].attrib
root[0][0].text

# xpath
root.find(".")  # 顶级元素

# 查找第一个遇到的匹配元素
root.find("./book/title").text

# 查找所有匹配的元素
root.findall("./book/title")
root.findall(".//*[@lang='en']")

# 返回匹配元素的文本值
root.findtext(".//*[@lang='en']")
root.findtext(".//*[@category='WEB']/year")

# 构建 XML
# 构建一个元素
a = ET.Element("a")
# 设置属性
a.set("语言", "中文")
# 构建一个 a 下面的子元素
b = ET.SubElement(a, "b")
c = ET.Element("c")
# 追加子元素
a.append(c)
# 移除 b
a.remove(b)
# 写入文件
# 构建结构树
tree = ET.ElementTree(a)
tree.write("demo/text1.xml", encoding="utf-8")

# 将元素数打印到 sys.stdout 调试用途
ET.dump(a)
