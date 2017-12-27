f = open("D:\python_workspace\Jumptopy\Chapter5\연습문제\poll.txt",'a')
f.close()

print("poll.txt 파일이 없습니다. 아래 중 선택하세요")
print("1. 종료")
print("2. 변경된 파일 경로 입력")
if int(input()) == 1:
    print("프로그램을 종료합니다.")
if int(input()) == 2:
    print("변경된 파일 경로를 입력하세요 : ")