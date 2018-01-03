
while True:
    n = int(input("홀수를 입력하세요:['0'=종료]"))
    if n <= 0:
        print('마름모 프로그램 출력을 이용해 주셔서 감사합니다.')
        break
    elif n % 2 == 0:
        print('짝수를 입력하였습니다. 재입력 부탁드립니다.')
    else:
        for i in range(1, n+1, 2):
            print(('*'*i).center(n, ' '))
        for i in range(n-2, 0, -2):
            print(('*' *i).center(n, ' '))