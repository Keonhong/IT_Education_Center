# try:
#    <예외 발생 예상 구문>
# except <예외 종류>
#    <예외 처리 문장>
# except <예외 종류1, 예외 중류2>
#    <예외 처리 문장>
# except 예외 as 파라메터
#    <예외 처리 문장>
# else:                     #생략 가능
#    <예외가 발생하지 않을 때 처리 문장>
# finally:                  #생략 가능
#    <예외와 상관없이 무조건 try 블록 이후 수행 할 문장>

a = [1, 2, 3]

try:
    a[0] / 0
except ZeroDivisionError:
    print(' 0으로 나눌 없습니다. ')

except IndexError:
    print(' 인덱스를 벗어났습니다. ')

except TypeError:
    print(' Type이 맞지 않아요. 문자열과 덧샘 불가. ')

a = [1, 2, 3]

try:
    a[5] = 5
except ZeroDivisionError:
    print(' 0으로 나눌 없습니다. ')

except IndexError:
    print(' 인덱스를 벗어났습니다. ')

except TypeError:
    print(' Type이 맞지 않아요. 문자열과 덧샘 불가. ')

# try ~ except

a = [1, 2, 3]

try:
    a[1] + 'korea'
except ZeroDivisionError:
    print(' 0으로 나눌 없습니다. ')

except IndexError:
    print(' 인덱스를 벗어났습니다. ')

except TypeError:
    print(' Type이 맞지 않아요. 문자열과 덧샘 불가. ')