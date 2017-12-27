# OrderedDict 란?
# OrderedDict는 기본 딕셔너리와 거의 비슷하지만, 입련된 아이템들의 순서를 기억하는 Dictionary
# 클래스이다. OrderedDict는 아이템들의 입력 순서를 기억하기 때문에 sorted()함수를 사용하여
# 정렬된 딕셔너리를 만들때 사용 할 수 있다. 아래[예제1]은 sorted dictionary를 만드는 예제이다.

# 예제1 - sorted()를 이용한 정렬된 orderedDict 만들기

from collections import OrderedDict

#기본 딕셔너리
d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}

# key를 기준으로 정렬한 OrderedDict
ordered_d1 = OrderedDict(sorted(d.items(), key = lambda t:t[0]))
print(ordered_d1)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# value를 기준으로 정렬한 OrderedDict
ordered_d2 = OrderedDict(sorted(d.items(), key = lambda t:t[1]))
print(ordered_d2)
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# key의 길이(len)를 기준으로 정렬한 OrderedDict
ordered_d3 = OrderedDict(sorted(d.items(), key = lambda t:len(t[0])))
print(ordered_d3)
# OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])

# ordered_d1에 새로운 아이템 추가
ordered_d1.update({'grape':5})
print(ordered_d1)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1), ('grape', 5)])

