# OrderedDict.Move_to_end()는 메소드는 key가 존재할 경우, (key,value)를 맨 오른쪽(뒤) 또는
# 맨 왼쪽(앞)으로 이동해주는 메소드이다. move_to_end(key, last=True)의 인자인 last=는 True일
# 경우 맨 오른쪽(뒤)로 이동하고, False인 경우 맨 왼쪽(앞)으로 이동한다.

# OrderedDict.move_to_end()

import operator
from collections import OrderedDict

# 기본 딕셔너리
d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}

# key를 기준으로 정렬한 OrderedDict
ordered_d = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=False))
print(ordered_d)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# move_to_end(key, last=True)인 경우: 해당 (key,value)가 맨 오른쪽(뒤)으로 이동함
ordered_d.move_to_end('banana', last=True)
print("move_to_end('banana', last=True) >>> {}".format(ordered_d))
# move_to_end('banana', last=True) >>> {} OrderedDict([('apple', 4), ('orange', 2), ('pear', 1), ('banana', 3)])

# move_to_end(key, last=False)인 경우: 해당 (key,value)가 맨 왼쪽(앞)으로 이동함
ordered_d.move_to_end('banana', last=False)
print("move_to_end('banana', last=False) >>> {}".format(ordered_d))