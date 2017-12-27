class Restaurant:
    number_served = 0
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describ1e_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다." %(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요." %(self.restaurant_name))
    def set_number_served(self,number):
        self.number_served1 = number
        print("오늘 방문한 고객은 %s명 입니다." % (self.number_served1))
    def increment_number_served(self,number):
        self.number_served = number + self.number_served
        print("오늘 총방문수는 %s명 입니다." % (self.number_served))

restaurant = Restaurant("빈센트","스테이크")
art = Restaurant("빈센트","스테이크")
art.describe_restaurant()
art.open_restaurant()

restaurant.set_number_served(0)
restaurant.increment_number_served(20)
restaurant.increment_number_served(20)
restaurant.increment_number_served(20)
restaurant.increment_number_served(20)

f = open("D:\python_workspace\Jumptopy\Codding_Test\고객서빙현황로그.txt",'r')
line = f.readlines()
f.close()
f = open("D:\python_workspace\Jumptopy\Codding_Test\고객서빙현황로그.txt",'a')
a=line[-1]
b=int(a)+restaurant.number_served
f.write(str(b)+'\n')
f.close()