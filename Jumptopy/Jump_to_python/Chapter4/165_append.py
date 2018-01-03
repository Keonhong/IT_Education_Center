#파일안에 내용 추가시키기
f = open("D:/python_workspace/Jumptopy/chapter4/새파일.txt",'a')
for i in range(11,21):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()