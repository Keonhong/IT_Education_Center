def getTotalpage(m,n):
    if int(m) % int(n) > 0:
        pages = int(m) // int(n) + 1
        print("게시물 총 건수 =",m, "한 페이지에 보여줄 게시물 수 =", n, "총 페이지 수 = ", pages)
    elif int(m) % int(n) == 0:
        pages = int(m) // int(n)
        print("게시물 총 건수 =",m, "한 페이지에 보여줄 게시물 수 =", n, "총 페이지 수 = ", pages)
f = open('D:\python_workspace\Jumptopy\Codding_Test\condition.txt','r')
read = f.read()
read_split = read.split()
count = 0
for i in read_split:
    A = []
    A.append(i)
    if count < 1:
        count = count + 1
        m = A[0]
    else:
        n = A[0]
        count = 0
        try:
            getTotalpage(m, n)
        except ValueError:
            pass
            f.close()
# print(getTotalpage(5,10))
# print(getTotalpage(15,10))
# print(getTotalpage('dfdf dfdf'))
# print(getTotalpage(25,10))
# print(getTotalpage(30,10))