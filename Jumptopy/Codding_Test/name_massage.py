#이름 반복/환영 메세지 출력
number = 0
while True:
    name = input("안녕하세요. 이름을 입력하세요: ")
    number += 1
    if number == 1:
        print("Hi %s!! You are %dst person come here!"% (name,number))
    elif number == 2:
        print("Hi %s!! You are %dnd person come here!"% (name,number))
    elif number == 3:
        print("Hi %s!! You are %drd person come here!"% (name,number))
    elif number < 11:
        print("Hi %s!! You are %dth person come here!"% (name,number))
    else:
        print("Sorry %s. The event is closed because You are 11th person come here."% name)