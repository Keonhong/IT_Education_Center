#연습생 아이돌 만들기
def show_list():
    for i in list:
        print(i,end = "")
    print()
def make_idol():
    count = 0
    for i in list:
        count += 1
        if count!= linecount:
            i = i[:-1]
        print('신예 아이돌 %s 인기 급상승'% i)

def make_world_star():
    count = 0
    for i in list:
        count += 1
        if count != linecount:
            i = i[:-1]
        print('아이돌 %s 월드스타 등극'% i)

f = open("D:\python_workspace\Jumptopy\Codding_Test\연습생.txt",'r')
list = []
linecount = 0
while 1:
    line = f.readline()
    if not line:
        break
    list.append(line)
    linecount += 1
show_list()
make_idol()
make_world_star()
f.close()