# 모듈 : 필요한 기능만 모아놓은 파일 (함수나 클래스)
# 확장자는 .py

from datetime import date
import random

from theater_module import price
print(random.random())
print(random.uniform(10, 20))
print(random.randrange(10))
print("[1,2,3,4,5] : ", random.choice([1,2,3,4,5]))
print("[1,2,3,4,5] : ", random.shuffle([1,2,3,4,5]))
print("[1,2,3,4,5] : ", random.sample([1,2,3,4,5], k=2))

# as 사용해서 단축하기 
import random as r
print(r.random())
print(r.uniform(10, 20))
print(r.randrange(10))
print("[1,2,3,4,5] : ", r.choice([1,2,3,4,5]))
print("[1,2,3,4,5] : ", r.shuffle([1,2,3,4,5]))
print("[1,2,3,4,5] : ", r.sample([1,2,3,4,5], k=2))

# 필요한거만 import 시키기
from random import random, uniform, randrange, choice, shuffle, sample 
print(random())
print(uniform(10, 20))
print(randrange(10))
print("[1,2,3,4,5] : ", choice([1,2,3,4,5]))
print("[1,2,3,4,5] : ", shuffle([1,2,3,4,5]))
print("[1,2,3,4,5] : ", sample([1,2,3,4,5], k=2))

# datetime 모듈 : 날짜와 시간관련 모듈 
import datetime
now = datetime.datetime.now()
print("현재 시각을 출력합니다 : ", now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 시간을 출력 
output = now.strftime("%y/%m/%d %H:%M:%S ")
print(output)

# timedelta : 두 날짜 사이의 간격 
today = datetime.date.today()
td = datetime.timedelta(days = 100) # 100일 저장 
print("우리가 만난지 100일은", today+td)

import time
print("지금부터 5초 동안 정지합니다")
print(time.sleep(5))
print("프로그램을 종료합니다")


# urllib
# from urllib import request
# target = request.urlopen("https://www.naver.com")
# output = target.read()

# print(output)


# 극장에서 현금만 받는다. 잔돈을 바꿔주지않는다. 정확히 사람수에 따라 가격이 얼마인지 계산하는 모듈 
# theater_module.py로 만들기 (현 프로젝트 폴더와 같은 경로에 만들기)

import theater_module
theater_module.price(3) # 3명 일반가격 
theater_module.price_morning(4) # 조조할인 가격 
theater_module.price_soldier(5) # 군인할인 가격 
print()

import theater_module as tm 
tm.price(3)
tm.price_morning(4)
tm.price_soldier(5)
print()

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)
print()

from theater_module import price, price_morning # 필요한 함수만 명시 
price(3)
price_morning(4)
price_soldier(5)
print()

from theater_module import price_soldier as price # 필요한 함수만 명시하고 그것을 별명을 붙여 사용
price(5)
print()


# 패키지 : 여러 모듈들을 모아놓은 것 (다른 사람이 만든 패키지 확인 사이트 : pypi.org, pip install xxx)

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel.vietnam import VietnamPackage
trip_to = VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to2 = thailand.ThailandPackage()

