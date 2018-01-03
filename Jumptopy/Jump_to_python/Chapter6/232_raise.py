number = int(input("숫자를 입력하세요."))
try:
    if(number<0):
        raise ValueError
except ValueError:
    print("음수 입력")