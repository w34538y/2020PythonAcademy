class unit:
    def __init__(self, name, hp, damage): # 생성자 (객체 또는 인스턴스를 생성할때 호출)
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

    def attack(self, name, location, damage):
        print("{0}:{1} 방향으로 적군을 공격합니다. 공격력[{2}]".format(self.name, location, self.damage))

# 마린: 공격유닛, 군인, 총을 쏠 수 있다
name = "마린" #유닛 이름
hp = 40 # 유닛 체력
damage = 5 # 유닛 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격유닛, 탱크, 포를 쏠수있다 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

marin = unit("마린",40,5)
tank = unit("탱크", 150,35)
tank2 = unit("탱크2", 150,35)

marin.attack(marin.name,"1시",marin.damage)
tank.attack(tank.name,"1시", tank.damage)
tank2.attack(tank2.name,"1시", tank2.damage)



class House:
    def __init__(self, location, house_type, deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}년")

houses =[]
house1 = House("강남", "아파트", "매매", "10억", "2018")
house2 = House("마포", "오피스텔", "전세", "5억", "2007")
house3 = House("송파", "빌라", "월세", "500/50", "2000")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {} 채의 매물이 있습니다.".format(len(houses)))

for house in houses:
    house.show_detail()