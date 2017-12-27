import time as t

t1 = t.time()
print('1970년1월1일0시부터 현재까지 흘러온 시간 : {}초'.format(int(t1)))

t2 = t.gmtime()
print(t2)

print('\n UTC 시간 ')
print('{}년{}월{}일'.format(t2.tm_year, t2.tm_mon, t2.tm_mday))
print('{}시{}분{}초'.format(t2.tm_hour, t2.tm_min, t2.tm_sec))

t3 = t.localtime()

print('\n local - 내컴퓨터 시간 ')
print('{}년{}월{}일'.format(t3.tm_year, t3.tm_mon, t3.tm_mday))
print('{}시{}분{}초'.format(t3.tm_hour, t3.tm_min, t3.tm_sec))
