def sumCount(str):
    result = {}
    s = ""
    for i in str.split(" "):
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


s = sumCount("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
print(s)
