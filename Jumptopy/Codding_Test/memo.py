import sys

option = sys.argv[1]
memo = sys.argv[2]
daemonja = []

if option == "-a":
    try:
        f = open("D:\python_workspace\Jumptopy\Codding_Test\memo.txt",'r')
        f.close()
        f = open("D:\python_workspace\Jumptopy\Codding_Test\memo.txt",'a')
        f.write(memo)
        f.write('\n')
        f.close()
        print(memo)
    except FileNotFoundError as e:
        e = print("memo.txt 파일이 없습니다. 아래 중 선택하세요")
        print("1.새로 생성하시겠습니까?")
        print("2.파일 경로를 입력하겠습니다.")
        a = int(input(":"))
        if a == 1:
            f = open("D:\python_workspace\Jumptopy\Codding_Test\memo.txt", 'w')
            f.write(str(memo))
            f.write('\n')
            f.close()
            print(memo)
        elif a == 2:
            route = str(input("파일 경로를 입력하겠습니다."))
            f = open(route + 'memo.txt', 'a')
            f.write(str(memo))
            f.write('\n')
            print(memo)
            f.close()
elif option == "-au":
    f = open("D:\python_workspace\Jumptopy\Codding_Test\memo.txt",'a')
    daemonja.append
    a = memo.upper()
    f.write(str(a))
    print(memo.upper())
    f.write('\n')
    f.close()
elif option == "-v":
    try:
        f = open("D:\python_workspace\Jumptopy\Codding_Test\memo.txt",'r')
        line = f.read()
        f.close()
        print(line)
    except FileNotFoundError as e:
        e = print("memo.txt 파일이 없습니다. 아래 중 선택하세요")
        print("1. 종료하시겠습니까?")
        print("2. 파일 경로를 입력하세요.")
        b = int(input(":"))
        if b == 1:
            print("종료되었습니다")
        if b == 2:
            route = str(input("변경된 파일 경로를 입력하세요. :"))
            f = open(route + 'memo.txt','r')
            line = f.read()
            f.close()
            print(line)

#D:\python_workspace\Jumptopy\Codding_Test\memo.py\memo.txt