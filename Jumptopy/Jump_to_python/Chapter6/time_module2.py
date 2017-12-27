import time as t

t2 = t.gmtime()

#요일 구하기

if t2.tm_wday ==0:
    w = '월'
elif t2.tm_wday ==1:
    w = '화'
elif t2.tm_wday ==2:
    w = '수'
elif t2.tm_wday ==3:
    w = '목'
elif t2.tm_wday ==4:
    w = '금'
elif t2.tm_wday ==5:
    w = '토'
elif t2.tm_wday ==6:
    w = '일'
else :
    pass
print('오늘은 {}요일입니다.'.format(w))