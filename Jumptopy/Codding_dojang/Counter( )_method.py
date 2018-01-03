# 1)update()
import collections

# 문자열
a = collections.Counter()
print(a)
a.update("aabbccccdeeeffgg")
print(a)
# Counter({'c': 4, 'e': 3, 'a': 2, 'b': 2, 'f': 2, 'g': 2, 'd': 1})

# 딕셔너리
a.update({'f':3, 'e':2})
print(a)

# 2)elements() >>> 해당 값을 풀어서 반환// 요소는 무작위// 대소문자 구분하며 sorted()로 정렬가능

import collections

c = collections.Counter("Hello Python")
print(list(c.elements()))
print(sorted(c.elements()))

c2 = collections.Counter(a=4,b=2,c=0,d=-2)
print(sorted(c2.elements()))
# ['a', 'a', 'a', 'a', 'b', 'b']

# 3)most_common(n) >>> 빈도수가 높은 순으로 상위 n개를 리스트안의 튜플형태로 반환

c3 = collections.Counter('apple, orange, grape, pear')
print(c3.most_common())
print(c3.most_common(3))

# 4)subtract() >>> 요소를 빼는 것을 말한다. 다만 요소가 없는 경우 음수의 값이 출력된다.

c4 = collections.Counter('hello python')
c5 = collections.Counter('i love python')
c4.subtract(c5)
print(c4)
# Counter({'h': 1, 'l': 1, 'e': 0,, ' 'o': 0, 'p': 0, 'y': 0, 't': 0, 'n': 0, ' ': -1i': -1, 'v': -1})

z = collections.Counter(a=4, b=2, c=0, d= -2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(z)
# Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})

# 3. Counter를 이용한 연산
# collections.Counter()는 산술/집합 연산이 가능하다.

a = collections.Counter(['a','b','c','b','d','a'])
b = collections.Counter('aaeroplane')

print(a)
print(b)
print(a+b)
'''(a) Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
   (b) Counter({'a': 3, 'e': 2, 'r': 1, 'o': 1, 'p': 1, 'l': 1, 'n': 1})
  (a+b)Counter({'a': 5, 'b': 2, 'e': 2, 'c': 1, 'd': 1, 'r': 1, 'o': 1, 'p': 1, 'l': 1, 'n': 1})
'''

x = collections.Counter('aabbccdd')
y = collections.Counter('abbbce')

print(x-y)
# Counter({'d': 2, 'a': 1, 'c': 1})

# Counter의 교집합 및 합집합의 출력값은 {값:개수}의 딕셔너리 형태로 반환된다.

r = collections.Counter('aabbccdd')
q = collections.Counter('abbbce')

print(r & q)
print(r | q)
# Counter({'b': 2, 'a': 1, 'c': 1})
# Counter({'b': 3, 'a': 2, 'c': 2, 'd': 2, 'e': 1})