#샌드위치 만들기.
def input_ingredient():
    material = []
    while True:
        print("안녕하세요, 원하시는 재료를 입력하세요: ")
        a = input()
        if a == '종료':
            return material
        material.append(a)
def make_sandwichs(material):
    print("샌드위치를 만들겠습니다.")
    for i in material:
        print("%s를 추가합니다."% i)
    print("여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요.")

while True:
    print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.")
    print("1.주문 2.종료 입력: ")
    order = input()
    if order == '1':
        material=input_ingredient()
        make_sandwichs(material)
    else:
        break