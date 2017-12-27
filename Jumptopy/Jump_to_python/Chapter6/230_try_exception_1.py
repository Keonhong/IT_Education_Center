# try/except 유형2
try:
    f=open('나없는파일','r')
    4/0
except ZeroDivisionError:
    print("0으로 나누었음")
except FileNotFoundError:
    print("없는 파일을 열었음")

print("End")