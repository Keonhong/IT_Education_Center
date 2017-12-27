while True:
    q = input("숫자를 입력하세요. (-1: 종료 all: 구구단 전체 출력) :")
    if q == '-1':
        break
    if q == 'all':
        for i in range(2,10):
            print(" "+"< " + str(i) + "단 >")
            for j in range(1, 10):
                print(i, "*", j, "=", i*j)
                continue
    try:
        if int(q) < 0:
            raise ValueError
    except ValueError:
        print("음수를 입력하였습니다. 양수를 입력해주세요.")
    else:
        q = int(q)
        print(" " + "< " + "%s단 >"% q)
        for j in range(1, 10):
            print(q, "*", j, "=", q*j)