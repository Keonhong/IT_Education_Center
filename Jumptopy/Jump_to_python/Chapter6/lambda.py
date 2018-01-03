def Add(a,b):
    return a + b
def Pow(a,b):
    tmp = 1
    for i in range(b):
        tmp = tmp * a
    return tmp

print(Add(10,30))
print(Pow(2,3))
print(Add(3,5))
print(Pow(2,10))

print((lambda a,b: a+b)(3,10))
print((lambda a,b: a+b)(100,300))
f1 = lambda a,b : a+b
print(f1(30,50))
print((lambda a,b: a**b)(2,3))
f2 = lambda a,b : a**b
print(f2(2,8))

for i in range(1,11):
    print(f2(2,i))

def Add(a,b):
    return a + b
f3 = Add
print(f3(4,5))