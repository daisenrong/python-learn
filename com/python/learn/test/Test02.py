import time

a = 1
b = 1.1
c = True
d = "ddd"

a = 11
b = 2.1
c = False
d = "dd+dd"

print(a)
print(b)
print(c)
print(d)
print(-7 // 2)

list = [1, 2, 3, 4]

for i in list:
    if (i == 3):
        pass
    print(i)

file = open("/Users/daisenrong/Desktop/1.txt")
str = file.readline()
print(str)


# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
