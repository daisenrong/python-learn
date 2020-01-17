def printStr(str):
    # 这里写你的逻辑  将字符串拆分成字母，然后大小写互换打印
    for i in str:
        print(i.swapcase())

n = input("请输入字符串：")

printStr(n)

