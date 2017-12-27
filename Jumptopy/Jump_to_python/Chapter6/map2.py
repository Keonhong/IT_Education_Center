d1 = {1:'one', 2:'two', 3:'three'}

def Add(a):
    return a + a

def Mul(a):
    return a * a

ret1 = list(map(Add, d1))
print(ret1)

ret2 = list(map(Mul, d1))
print(ret2)

ret1 = list(map(Add, [d1[i]for i in d1]))
print(ret1)

ret2 = list(map(Mul, [d1[i]for i in d1]))
print(ret2)

#문자열끼리 +는 되고, *는 안된다.