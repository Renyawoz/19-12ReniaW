a = 9

def pierwsz():
    global a
    a = 1
    b = 2
    return a + b

def druga():
    c = 3
    return a + c


print(pierwsz())
print(druga())
print(a)