def yhm(y):
    if y == "abc":
        return True
    return False


def mm(y):
    if y == "123":
        return True
    return False


username = input("username:")
pwd = input("pwd:")

if yhm(username) + mm(pwd) < 2:
    print("fali")
else:
    print("ok")
