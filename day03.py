# 1. (1, 2, 3) 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 출력해보자 
a = (1, 2, 3)
print(a)
a = a + (4, )
print(a)
print()
print()

# 2. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자 
a = {'A' : 90, 'B' : 80, 'C' : 70}
# 딕셔러니의 pop함수를 사용해 보자 
result = a.pop('B')
print(a) # {'A' : 90, C' : 70}
print(result) # 80 출력 
print()
print()


# 3. fruit = {'apple' : 5, 'banana' : 5, 'graph' : 7, 'orange' : 3, 'peach' : 10}
fruit = {'apple' : 5, 'banana' : 5, 'graph' : 7, 'orange' : 3, 'peach' : 10}
# key들만 출력하시오.
print(fruit.keys())
# value만 출력하시오
print(fruit.values())
# 딕셔너리 자료 추가하기(원하는 과일이름으로 키를 만들고, 과일의 수를 값으로)
fruit['melon'] = 5
# key와 value 쌍으로 출력하시오 
print(fruit.items())
# 키가 안에 있는지 확인하기 
print('apple' in fruit)
print('kiwi' in fruit)
print()
print()

person = {'Name' : "홍길동", 'birth' : 1128, 'age' : 30}
print(person)
print()
print()

# 변수 #

# 변수 만들기 / 사용하기 
# 예시 - 원의 둘레와 넓이 구하기 
# 변수 선언과 할당
pi = 3.14159265
r = 10 

# 변수 참조 
print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2 * pi * r)
print("원의 넓이 = ", pi * r * r)
print()
print()

# input 함수 
#string = input("입력 A>")
#int_num = int(string)
#string2 = int(input("입력 B>"))
#print(int_num + string2)
print()
print()

# 다음 코드는 inch단위의 자료를 입력 받아 cm를 구하는 예제이다 
# 빈칸에 알맞은 내용을 넣어 코드를 완성하라 1inch = 2.54cm 

#str_input = input("숫자 입력 >")
#num_input = float(str_input)

print()
#print(num_input, "inch")
#print((num_input * 2.54), "cm")
print()
print()

# 원의 반지름을 입력 받아 원의 둘레와 넓이를 구하는 코드이다
# 빈칸에 알맞은 ㄴ애ㅛㅇ을 넣어 코드를 완성하라 

#str_input = input("원의 반지름 입력> ")
#num_input = float(str_input)
print()
#print("반지름 : ", num_input)
#print("둘레 : ", 2 * 3.14 * num_input)
#print("넓이 : ", 3.14 * num_input ** 2)
print()
print()

string_a = "{0}, {1}".format(10, 20)
print(type(string_a))
print()
print()

output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print()
print()

name = "홍길동"
age = 20
print("name: {0}이고, age: {1}살 입니다".format(name, age))
print(f"name: {name}이고, age: {age}살 입니다") # 파이썬 3.6 이상부터 가능
print()
print()

# strip() 함수 
a = "       Python is the best choice     "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# find(), index() - 문자열에서 내가 찾는 문자의 위치를 알려줌 
print(a.index("i"))
print("Python" in a)

# split() - 문자열 리스트 변환방법 분할하기 
print(a.split(" "))
print(a.split(maxsplit = 2)) # 2개까지 나눈다. 그러면 문자열리스트가 3개의 요소를 갖게된다 
b = "a,b,c,d,e".split(",", maxsplit = 2)
print(b)
c = ''' Hello World
i love python
i love chicken
'''
# 줄 단위 나누기 splitlines()
d = c.splitlines()
print(d)

# 3. 문자열 변경 수정 삭제(replace()) 예제
f = "Hello World~ i love python~ i love chicken"
print(f.replace("~", "!"))
print(f.replace("~", "!", 1))
print(f.replace("~", ""))
print(f.replace("", ""))

# join()
print(", ".join("with"))


# 확인문제 
a = input("> 1번째 숫자 : ")
b = input("> 2번째 숫자 : ")
print()

print("{} + {} = {}".format(a, b, int(a) + int(b)))

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 추첨 프로그램을 작성하시오 

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20으로 가정 
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가 
# 조건3 : random 모듈의 shuffle과 sample을 활용 

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *
lst = range(1,20) # 1~20 숫자 생성 
lst = list(lst) # 타입 변환
shuffle(lst)
winner = sample(lst, 4) # 4명 중에서 1명은 치킨, 3명은 커피 
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0} ".format(winner[0]))
print("커피 당첨자 : {0} ".format(winner[1:]))
print("-- 축하합니다 --")