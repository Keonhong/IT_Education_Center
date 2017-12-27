def plus(a,b):
    sum = a+b
    return sum

while True:
    num = input("안녕하세요. 두 수를 입력하세요. ('종료' 프로그램종료) : ").split()
    if "종료" in num:
        print('프로그램을 종료합니다.')
        break
    try:
        a=int(num[0])
    except:
        print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (1,num[0]))
        continue
    try:
        # a = int(num[0])
        b = int(num[1])
    except:
        print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (2,num[1]))
        continue
    print(plus(a,b))
