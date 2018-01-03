f= open("D:/python_workspace/Jumptopy/chapter4/새파일.txt",'r')
#while True:
#    line =f.readline()
#    if not line: break
#    print(line,end='')

#lines = f.readlines()
#for line in lines:
#    print(line)

data=f.read()
print(data)
f.close()