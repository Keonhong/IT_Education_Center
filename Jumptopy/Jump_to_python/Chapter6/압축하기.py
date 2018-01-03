#aaabbcccccca입력값
#a3b2c6a1출력값

q = 'aaabbcccccca'
result = q[0]
count = 0

for i in q:
    if i == result[-1]:
        count += 1
    else:
        result += str(count)+ i
        count = 1
result += str(count)
print(result)