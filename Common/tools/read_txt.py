def read_txt(file):
    """读取txt文件的数据

    :param file: 文件路径
    :return:
    """
    L = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            # 去除换行符
            if line[-1] == "\n":
                line = line[:-1]
            # 去除空行
            if line == "":
                continue
            # 去除注释行
            if line[0] == "#":
                continue
            L.append(line.split("|"))  # 按 | 拆分并追加到列表中

    return L


if __name__ == "__main__":
    L = read_txt("../../Test_Data/login_user_password.txt")
    print(L)
