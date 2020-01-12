# username = input("username:")
# pwd = input("pwd:")
#
# if username=="abc" and pwd=="123":
#     print("ok")
# else:
#     print("fail")
a = "aaa"
b = [1, 2, 3]
c = [1, 2, 3]
print("str" * 3)

print(b == c)
print(b is c)
a = "vvv"
print(a)

s = (1, 2, 34, 1, 1)
print(s)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # a 和 b 的差集

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# listNew = list[::-1]

for i in list[::-1]:
    if i % 2 != 0:
        print(i)

print("0---------------------------------------------------------------------")
print(-1 and -2)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(1 in list)
print(list == list2)
print(list is list2)

print("0---------------------------------------------------------------------")
a = 9
print(a)
# del a
# print(a)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list)
del list[0]
print(list)
a = 2e2

# if a > 2:
#     if a < 10:
#         print("<10")
#     else:
#         print(">=10")
# else:
#     print("<2")
#
# if a > 2 and b < 10:
#     print(">2 an <10")
# elif a > 2 and b >= 10:
#     print(">2 an >=10")
# else:
#     print("<2")

def getSum(a,b):
    a+=1
    b+=2

aa=1
bb=2
print(aa)
print(bb)
getSum(aa,bb)
print(aa)
print(bb)

def delList(list):
    del list[0]

list = [1,2,3]
print(list)
delList(list)
print(list)