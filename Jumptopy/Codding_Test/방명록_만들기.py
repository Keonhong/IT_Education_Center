f = open("D:\python_workspace\Jumptopy\Codding_Test\방명록.txt",'r')
# f.write("홍길동 800912\n손미나 901223\n") 프로그램을 구동했을때 다시 적게되어 이전에 적었던 내용 사라짐
f.close()

while True:
        print("이름을 입력하세요: ")
        f = open("D:\python_workspace\Jumptopy\Codding_Test\방명록.txt",'r')
        line = f.read()
        name = input()
        if name in line:
                print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요." % name)
                continue
        else:
                print("생년월일을 입력하세요(예:801212):")
        f.close()
        f = open("D:\python_workspace\Jumptopy\Codding_Test\방명록.txt",'a')
        data = input()
        f.write(name+' '+data+'\n')
        f.close()
        print("환영합니다. 즐거운 시간되세요.")