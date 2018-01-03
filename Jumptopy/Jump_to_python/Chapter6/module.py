import os

while 1:
    print('**** 메 뉴 ****')
    print('***************')
    print(' 1. 메모장')
    print(' 2. 계산기')
    print(' 3. 명령 프롬프트')
    print(' 0. 프로그램 종료')
    print('***************')

    menu = int(input(' 선택하세요 : '))

    if menu == 0:
        print(' Good - Bye! ')
        break
    if menu == 1:
        os.system('notepad')
    elif menu == 2:
        os.system('calc')
    elif menu == 3:
        os.system('cmd')
    else:
        continue