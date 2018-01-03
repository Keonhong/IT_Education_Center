# collections.nametuple()의 메소드들
# 1) _make(iterable)

import collections

# Person 객체 만들기
Person = collections.namedtuple("Person", 'name age gender')

P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')

# _make()를 이용하여 새로운 객체 생성
P3 = Person._make(['Peter', 24, '남'])
P4 = Person._make(['Ary', 23, '여'])

for n in [P1, P2, P3, P4]:
    print('%s은(는) %d세의 %s성 입니다.' % n)

# 2) _asdict() >>> 기존에 생선된 namedtuple()의 인스턴스(객체)를 OrderedDict로 변환하는 함수
# _asdict()를 이용하여 OrderedDict로 변환
print(P3._asdict())

# 3) _replace(kwargs) >>> 기존에 생성된 nametuple()의 인스턴스의 값을 변경할때 사용
# _replace()를 이용하여 인스턴스 값 변경

P1 = P1._replace(name='Neo')
P2 = P2._replace(age=27)
P3 = P3._replace(age=26)
P4 = P4._replace(name='Ari')
print('-'*20)
for n in [P1, P2, P3, P4]:
    print('%s은(는) %d세의 %s성 입니다.' % n)

# 4) _fields >>> 생성된 namedtuple()dml 필드명(field_names)를 tuple()형식으로 return해준다.
# _fields를 이용하여 필드명 출력
print(P1._fields)
# ('name', 'age', 'gender')

# 5) getattr() >>메소드는 아니지만 field_names로 namedtuple() 인스턴스의 값을 추출해준다.
print(getattr(P1,'name'))
print(getattr(P2, 'gender'))
print(getattr(P3, 'age'))
print(getattr(P4, 'age'))

# 6) dictionary에서 namedtuple()로 변환(**dict)
# double-star-operator(**)는 딕셔너리를 namedtuple()로 변환해준다.

dic = {'name': 'Tom', 'age':24, 'gender': '남'}
P3 = Person(**dic)

for n in [P1,P2,P3,P4]:
    print('%s은(는) %d세의 %s성 입니다.'% n)
    print(n)