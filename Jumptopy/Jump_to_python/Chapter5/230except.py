def check_number():
    if(number<0):
        # print("양수를 입력하세요.")
        raise ValueError
try:
    number = int(input("양수를 입력하세요: "))
    if(number<0):
        # print("양수를 입력하세요.")
        raise NegativeNumberInputError
    # f=open("나없는파일",'r')
    # 4/0
    print("Hello world")
except FileNotFoundError as e:
    print("없는 파일을 열었습니다.")
    print("시스템 에러 메세지: "+str(e))

except ZeroDivisionError:
    # print("에러가 발생했습니다.")
    print("0으로 나누었습니다.")

except ValueError as e:
    print("잘못된 값을 입력하셨습니다.")
    print("시스템 에러 메세지"+str(e))
else:
    print("Thank you!!")

finally:
    print("See ya")

print("프로그램 정상 종료")
