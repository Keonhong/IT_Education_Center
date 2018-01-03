#isinstace 함수
class Person: pass
a = Person()
print(isinstance(a,Person))

#lambda 함수
sum = lambda a,b:a+b
print(sum(3,4))
Mylist = [lambda a,b:a+b, lambda a,b:a*b]
print(Mylist[0](3,4))
print(Mylist[1](3,4))

#len 함수
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

#map 함수
#(함수 사용전)
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)
#(함수 사용후)
def two_times(x):return x*2
print(list(map(two_times, [1,2,3,4])))
#(여기에 lambda 함수응용)
print(list(map(lambda a: a*2,[1,2,3,4])))

#range 함수
print(list(range(5,101,5)))