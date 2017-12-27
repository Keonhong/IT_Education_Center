def sumDivisor(num):
    result = 0

    for i in range(1,num+1):
        if num % i == 0:
            result += i

    return  result
print(sumDivisor(14))

def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num % i == 0])

print()