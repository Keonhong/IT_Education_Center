f=open("D:\python_workspace\Jumptopy\Chapter5\연습문제\learning_python.txt",'r')
ff=open("D:\python_workspace\Jumptopy\Chapter5\연습문제\learning_python_copyed.txt",'w')

# line=f.readline()
# str_a=line.replace("python","C")
# ff.write(str_a)
# f.write(replaceAll)
# print(f=open("D:\python_workspace\Jumptopy\Chapter5\연습문제\learning_python_copyed.txt",'w'))
# line=f.readline()
# str_a=line.replace("python","C")
# ff.write(str_a)
# line=f.readline()
# str_a=line.replace("python","C")
# ff.write(str_a)
# f.close()
# ff.close()

line=f.readlines()
for i in line:
    i = i.replace("python","C")
    ff.write(i)
f.close()
ff.close()