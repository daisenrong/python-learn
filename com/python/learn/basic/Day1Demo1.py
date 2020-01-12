import keyword


def demo1():
    # 关键字

    print(keyword.kwlist)

    # 注释
    # 第一个注释
    # 第二个注释

    '''
    第三注释
    第四注释
    '''

    """
    第五注释
    第六注释
    """

    # 数据类型
    a = 1
    b = 1.1
    b1 = 1e3
    c = True
    d = 1 - 9j

    print(a)
    print(b)
    print(b1)
    print(c)
    print(d)

    # String
    str1 = """ aaa
    fasdf"""

    # 转义
    str2 = "换行 \n ok"
    str3 = r"换行 \n fail"

    print(str2)
    print(str3)

    # 拼接
    str4 = "lalala"
    str5 = "lalala"
    print(str4 + str5)
    print("lalala" "lalala")
    print(str4 * 2)
    print("la" * 3)

    # 截取
    strName = "python"
    print(strName[0:1])  # 左闭 右开
    print(strName[0:10])  # 左闭 右开 不存在角标越界问题
    print(strName[0:-1])  # 左闭 右开

    # 用户输入
    # username = input("\n username:")
    # print(username)

    import sys

    # 同一行显示多条语句
    _不建议 = "不建议啊";
    sys.stdout.write(_不建议)
    print()

    for i in sys.argv:
        print(i)

    from sys import argv, path

    print(argv)
    print(path)


def testList():
    list = [1, 2, 3, 4, 5]
    listCopy = [1, 2, 3, 4, 5]
    print(list[0:])  # 全部
    print(list[0:1])  # 0开始，1结束 左闭右开
    print(list[0:-1]) # 0开始，1结束 左闭右开

    print(list)
    print(list*2)
    print(list+list)

    list.append(1)
    print(list)
    listNew = list.copy()  # 深拷贝
    list[0]="a"
    print(list)
    print(listNew)



testList()
