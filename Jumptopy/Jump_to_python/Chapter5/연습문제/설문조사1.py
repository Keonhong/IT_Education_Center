f = open("D:\python_workspace\Jumptopy\Chapter5\연습문제\poll.txt",'r')
f.close()
while True:
    q = input("프로그래밍이 왜 좋으세요?('종료' 입력 시 프로그램 종료) :")
    f = open("D:\python_workspace\Jumptopy\Chapter5\연습문제\poll.txt",'a')
    if q == "종료":
        break
    print("이름을 입력하세요:")
    name = input()
    f.write(['name']+'\n')
    f.close()
    print("설문에 응답해 주셔서 감사합니다.")