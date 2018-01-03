def Add(a):
    return a + a

def Mul(a):
    return a * a

b1 = [1,2,3,4,5]
b2 = [2,4,6,8,10]
print(type(b1))
print(type(b2))

ret1 = list(map(Add,b1))
print(ret1)
ret2 = list(map(Add,b2))
print(ret2)

s1 = {1,2,3,4,5}
s2 = {2,4,6,8,10}
print(type(s1),type(s2))

ret1 = set(map(Add, s1))
print(ret1)
ret2 = set(map(Add, s2))
print(ret2)

ret1 = set(map(Mul, s1))
print(ret1)
ret2 = set(map(Mul, s2))
print(ret2)