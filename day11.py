# 7월 27일 강의 

# 클래스와 객체 복습
class Calculator:
    def __init__(self, num1, num2): # self는 this와 비슷하다. 
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(result)

    def mul(self):
        result = self.num1 * self.num2
        print(result)

    def sub(self):
        result = self.num1 - self.num2
        print(result)

    def div(self):
        result = self.num1 / self.num2
        print(result)

c1 = Calculator(3,4) # 생성자
c1.add()
print(c1.mul())
print(c1.sub())
print(c1.div())


# 상속 
class MoreCalculator(Calculator):
    def pow(self):
        result = self.num1 ** self.num2
        return result

c2 = MoreCalculator(4,2)
print(c2.pow())
c2.add()


# class Unit:
#     def __init__(self, name, hp): # 생성자 (객체 또는 인스턴스를 생성할때 호출)
#         self.name = name
#         self.hp = hp

# # 공격 유닛 : Unit 상속 
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.name = name
#         Unit.hp = hp 
#         self.damage = damage
    
#     def attack(self, name, location, damage):
#         print("{0}:{1} 방향으로 적군을 공격합니다. 공격력[{2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))


# # 유닛 객체 생성(== 유닛 클래스 사용)
# marin = Unit("마린",40,5)
# tank = Unit("탱크", 150,35)
# tank2 = Unit("탱크2", 150,35)

# # 공격 유닛 객체인 firebat 생성
# firebat = AttackUnit("파이어뱃", 50, 25)
# firebat.attack("1시방향")
# firebat.damaged(25)
# firebat.damaged(25)

# # 공중 유닛 클래스 정의(날수 있는 기능, 공격불가)
# class Flyable:
#     def __init__(self):
#         self.flying_speed = flying_speed
#     def fly(self):
#         print(f"{name} : {location} 방향으로 날아갑니다 [속도: {self.flying_speed}]")

# # 공중 공격 클래스 정의 (다중 상속)
# class  AttackFlyable(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# # 발키리 객체 생성 (공중공격유닛)
# valkyrie = AttackFlyable("발키리", 50, 16, 20)
# valkyrie.attack("1시")
# valkyrie.fly(valkyrie.name, "1시")

# 메소드 오버로딩(재정의)
# 기존 클래스를 수정함

# 일반유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자 (객체 또는 인스턴스를 생성할때 호출)
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]".format(self.name, location, self.speed))

# 공격 유닛 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, name, location, damage):
        print("{0}:{1} 방향으로 적군을 공격합니다. 공격력[{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name))

# 공중 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다 [속도: {self.flying_speed}]")

# 공중 공격 유닛 클래스 : 다중상속 
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩(재정의)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상유닛, 기동성이 좋음 
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력이 좋고, 공격력도 좋다 
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
#battlecrusier.fly(battlecrusier.name, "9시") # 매번 공중유닛은 fly만 호출, 지상유닛은 move만 호출 

# move를 새롭게 고쳤다 
battlecrusier.move("9시")


class Family:
    lastname = "감" # 클래스 변수 
    def __init__(self, first):
        self.lastname = first # 인스턴스 변수 

Family.lastname = "박"
print(Family.lastname)

a = Family("조")
b = Family("임")
print(a.lastname)
print(b.lastname)