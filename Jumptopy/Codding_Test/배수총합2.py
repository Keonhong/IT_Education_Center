q = input("범위, 첫번째수, 두번째수를 입력하세요. 종료: 프로그램종료-").split(' ')
x = q[0]
y = q[1]
v = q[2]
print("0부터 %s이하의 범위를 선택하셨습니다. 이 중에서"% x)
print("%s의 배수는"% y)

for i in range(1,int(x)+1):
    if i % int(y) == 0:
        print(i,end=' ')

print('\n'+"%s의 배수는"% v)
for j in range(1,int(x)+1):
    if j % int(v) == 0:
        print(j,end=' ')
print('\n'+"%s,%s의 배수는"% (y,v))

for z in range(1,int(x)+1):
    if z % int(y) == 0 or z % int(v) == 0:
        print(z,end=' ')
result = 0
for c in range(1,int(x)+1):
    if c % int(y) == 0 or c % int(v) == 0:
        result += c
print('\n'"따라서 총합은",result,"입니다.")