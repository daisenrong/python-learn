# 继承中的type 和isinstance
class Father(object):
    def __init__(self, name):
        self.name = name
        print(name)

    def getName(self):
        return self.name


class Son(Father):
    def getName(self):
        return "son" + self.name


f = Father("father")
s = Son("son")
print(f.getName())
print(s.getName())

print(Father == type(f))
print(isinstance(f, Father))

print(Father == type(s))
print(isinstance(s, Father))
