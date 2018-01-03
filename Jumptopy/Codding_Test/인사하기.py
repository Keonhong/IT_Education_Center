# 인사하기
# f=open("D:\python_workspace\Jumptopy\Codding_Test\인사하기.txt",'w')
# f.write("janny,hannah,margot,kevin,min\n")
# f.close()
#
# f=open("D:\python_workspace\Jumptopy\Codding_Test\인사하기.txt",'a')
# user_names=['janny!','hannah!','margot!','kevin!','min!']
# for i in user_names:
#     A = i[0:1]
#     a = A.upper()
#     N = i[1:]
#     insa = "Hello, %s%s\n" % (a,N)
#     f.write(insa)
# f.close()

import sys
args = sys.argv[1:]

def greet_users(username):
    usernames = username[0:1]
    usernames = usernames.upper()
    print("Hello, %s" % usernames,end="")
    print("%s!"%username[1:])

for i in args:
    greet_users(i)