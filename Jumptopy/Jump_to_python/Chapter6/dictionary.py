def myfun5(**kwargs):
    print(kwargs)

dic1 = {'1':'one', '2':'two', '3':'three'}
print(myfun5(**dic1))
print(myfun5(이름='홍길동', 나이=48949519231, 직업= '동해번쩍 서해번쩍'))

dic2 = {'one':1, 'two':2, 'three':3}

print(myfun5(**dic2))
print(myfun5(one = 1, two = 2))
print(myfun5(one = 1, two = 2, three = 3, four = 4, five = 5))
print(myfun5(나라 = '대한민국', 수도 = '서울', 인구 = 5000))