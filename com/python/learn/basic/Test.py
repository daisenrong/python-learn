str=input("请输入一句话：")
n={}

for i in str:
    n[i]=str.count(i)
    print i
print n