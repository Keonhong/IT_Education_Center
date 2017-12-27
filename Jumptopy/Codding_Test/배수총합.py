# q = input("범위, 첫번째 수, 두번째 수를 입력하세요. (종료: 프로그램 종료) : ").split(' ')
# x = q[0]
# y = q[1]
# z = q[2]
# print("0부터 %s이하의 범위를 선택하셨습니다. 이중에서" % x)
# for j in range(1,int(x)):
#     if j % int(y) == 0:
#         print(("%s의 배수는 ")% y)
#         print(j)
q = input("첫번째수 두번째수").split(' ')
x = q[0]
y = q[1]
print("3의 배수는")
input_range=15
for i in range(1,input_range+1):
    if i % int(x) == 0:
        print(i,end=' ')

print('\n'+"5의 배수는")
for j in range(1,input_range+1):
    if j % int(y) == 0:
        print(j,end=' ')
print('\n'+"%s,%s의 배수는"% (x,y))

for z in range(1,input_range+1):
    if z % int(x) == 0 or z % int(y) == 0:
        print(z,end=' ')
# print("따라서 1부터 15이하의 범위내에서"+%s+%s+"수의 총합은 a입니다."% (x,y))
result = 0
for c in range(1,input_range+1):
    if c % int(x) == 0 or c % int(y) == 0:
        result += c
print('\n'"따라서 총합은",result,"입니다.")