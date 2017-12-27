# print(abs(3))
# # print(abs(-3))
# # prin.t(abs(-1.2))
# # int_list = [1,2,3,4,5]

def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result
print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x > 0
print(list(filter(positive,[1,-3,2,0,-5,6])))

print(list(filter(lambda x: x> 0, [1,-3,2,0,-5,6])))