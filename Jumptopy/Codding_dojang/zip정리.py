#zip() 함수는 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.
#각 자료형의 i-th 에 해당하는 요소(elements)를 묶어주는 함수이다.

x = [1,2,3]
y = [4,5,6]

zipped = zip(x,y)
print(list(zipped))
#[(1, 4), (2, 5), (3, 6)]

z = [7,8,9]
zipped2 = zip(x,y,z)
print(list(zipped2))
#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#str형
a = 'abc'
b = 'def'

zipped3 = zip(a,b)
print(list(zipped3))
#[('a', 'd'), ('b', 'e'), ('c', 'f')]

#zip()을 이용해서 Dictionary의 {key:value} 중 value 값으로 최대값과 최소값,
#그리고 정렬하는데 사용 할 수 있다.

# 예제2 - zip()을 이용한 Dictionary의 value기준으로
# 최소(min), 최대(max)값 찾기 및 정렬하기
# 1) 최소, 최대값 찾기

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

min_item = min(zip(d.values(), d.keys()))
max_item = max(zip(d.values(), d.keys()))

print(min_item)
print(max_item)
#(1, 'pear') (4, 'apple')

# 2) 오름차순으로 정렬하기

d_sorted = sorted(zip(d.values(), d.keys()))
print(d_sorted)
#[(1, 'pear'), (2, 'orange'), (3, 'banana'), (4, 'apple')]

d_sorted2 = sorted(d.items(), key = lambda t:t[1])
print(d_sorted2)
#[('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)]

# itertools.zip_longest(*iterables, fillvalue=None)
# 3) 길이가 다른 자료형에 zip() 함수 적용

x = [1,2,3]
y = [4,5,6,7]

zipped = zip(x,y)
print(list(zipped))
#[(1, 4), (2, 5), (3, 6)]

#이렇게 길이가 다른 경우의 자료형에는 itertools.zip_longest()를 사용하면 된다.
#docs.python.org에서 살펴보면 길이가 다른 자료형인 경우
#zip_longest(*iterables, fillvalue=None)의 fillvalue= 인자에 값을 지정하여
# zip() 함수를 적용해준다.

from itertools import zip_longest

x = [1,2,3]
y = [4,5,6,7]

# 1) zip_longest 적용
zipped = zip_longest(x,y)
print(list(zipped))
#[(1, 4), (2, 5), (3, 6), (None, 7)]

# 2) fillvalue= 인자에 값을 지정
zipped = zip_longest(x,y, fillvalue=0)
print(list(zipped))
#[(1, 4), (2, 5), (3, 6), (0, 7)]