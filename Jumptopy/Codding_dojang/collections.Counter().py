# collections.Counter()의 결과값은 딕셔너리 형태로 출력된다.
# Counter()의 다양한 입력값들 1) 리스트(List)
import collections

lst = ['aa','cc','dd','aa','bb','ee']
print(collections.Counter(lst))
# Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})

# 2) 딕셔너리(Dictionary)
print(collections.Counter({'가':3, '나':2, '다':4}))
# Counter({'다': 4, '가': 3, '나': 2})

# 3) 값 = 개수 형태
# collections.Counter(a=2, b=3, c=2)는 ['a','a','b','b','b','c','c']와 같다.
c = collections.Counter(a=2, b=3, c=2)
print(collections.Counter(c))
print(sorted((c.elements())))
# Counter({'b': 3, 'a': 2, 'c': 2})
# ['a', 'a', 'b', 'b', 'b', 'c', 'c']

# 4) 문자열(String) >>> 문자열을 입력했을 경우 {문자:개수}의 딕셔너리 형태로 반환해 준다.
container = collections.Counter()
container.update("aabcdeffgg")
print(container)
# Counter({'a': 2, 'f': 2, 'g': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

for k,v in container.items():
    print(k,':',v)
