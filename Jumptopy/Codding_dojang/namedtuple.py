# namedtuple
# index로만 값에 접근 가능한 기본 tuple과는 다르게 key값으로 접근가능하도록 제공한다.
# namedtuple에서는 field_names를 가지고 값에 접근이 가능하다는 부분이 딕셔너리타입과
# 비슷하다고 할 수 있다.

# tuple() vs namedtuple()

a = ('john', 28, '남')
b = ('sally', 24, '여')
for n in [a,b]:
    print('%s은(는) %d 세의 %s성 입니다.' %n)

import collections

#namedtuple()
Person = collections.namedtuple("Person", 'name age gender')

P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')

for n in [P1,P2]:
    print('%s은(는) %d세의 %s성 입니다.' % n)

print(P1.name, P1.age, P1.gender)
print(P2.name, P2.age, P2.gender)