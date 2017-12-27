# popitem(last=True)
# OrderedDict.popitem(last=True) 메소드는 (key,value)로 OrderedDict의 아이템들을 반환
# 및 삭제하는 메소드이다. popitem()의 인자인 last= 는 True일 경우 LIFO방식으로 값을 반환 및
# 삭제하고, False일 경우 FIFO방식으로 값을 반환&삭제한다.

# OrderedDict.popitem()

import operator
from collections import OrderedDict

# 기본 딕셔너리
d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}

# key를 기준으로 정렬한 OrderedDict
ordered_d = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=False))
print(ordered_d)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# popitem(last=True)일 경우 LIFO방식으로 pop,default는 True임
# for i in range(len(ordered_d)):
#     print(ordered_d.popitem(last=True))
print('='*50)

# popitem(last=False)일 경우 FIFO방식으로 pop
for i in range(len(ordered_d)):
    print(ordered_d.popitem(last=False))