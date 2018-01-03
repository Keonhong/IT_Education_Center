def plus(a,b):
    sum = a+b
    return sum
def sub(a,b):
    sub = a-b
    return sub
def div(a,b):
    div = a/b
    return div
def multiple(a,b):
    mul = a*b
    return mul

while True:
    kind = int(input("""1.덧셈 2.뺄셈 3.나눗셈 4.곱셈
***필요한 사항을 선택해주세요*** : """))
    if kind == 1:
        print("덧셈을 선택하였습니다.")
        num = input("안녕하세요. 두 수를 입력하세요. ('종료' 프로그램종료) : ").split()
        try:
            int(num[0])
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (1,num[0]))
            continue
        try:
            a = int(num[0])
            b = int(num[1])
            print(plus(a,b))
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (2,num[1]))
    elif kind == 2:
        print("뺄셈을 선택하였습니다.")
        num = input("안녕하세요. 두 수를 입력하세요. ('종료' 프로그램종료) : ").split()
        try:
            int(num[0])
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (1,num[0]))
            continue
        try:
            a = int(num[0])
            b = int(num[1])
            print(sub(a,b))
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.'% (2,num[1]))
    elif kind == 3:
        print("나눗셈을 선택하였습니다.")
        num = input("안녕하세요. 두 수를 입력하세요. ('종료' 프로그램종료) : ").split()
        try:
            int(num[0])
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.' % (1, num[0]))
            continue
        try:
            int(num[0])/int(num[1])
        except:
            print("죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.")
            continue
        try:
            a = int(num[0])
            b = int(num[1])
            print(int(div(a,b)))
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.' % (2, num[1]))
    elif kind == 4:
        print("곱셈을 선택하였습니다.")
        num = input("안녕하세요. 두 수를 입력하세요. ('종료' 프로그램종료) : ").split()
        try:
            int(num[0])
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.' % (1, num[0]))
            continue
        try:
            a = int(num[0])
            b = int(num[1])
            print(multiple(a,b))
        except:
            print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요.' % (2, num[1]))