#영화관 티켓 판매기
while True:
    print("안녕하세요. IT영화관을 찾아주셔서 감사합니다.")
    a = int(input("나이를 입력하세요: (-1 종료)"))
    if a < 3 and a > 0:
        print("%s세의 입장료는 무료입니다. 감사합니다."% a)
        continue
    if a >= 3 and a < 13:
        print("%s세의 입장료는 10달러입니다. 감사합니다."% a)
        continue
    if a >= 13:
        print("%s세의 입장료는 15달러입니다. 감사합니다."% a)
        continue
    else:
        a == -1
        print("프로그램을 종료합니다.")
        break