a=1
def vartest(a):
    a=a+1

vartest(a)
print(a)

#함수밖의 a가 함수안에 적용되기 위한 조건

a=1
def vartest(a):
    a = a + 1
    return a

a=vartest(a)
print(a)

a=1
def vartest():
    global a
    a = a + 1
vartest()
print(a)