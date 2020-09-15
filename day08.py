# 7월 21일 강의 

# ======================== 함수 정의 복습 ========================
# 퀴즈1) 주어진 자연수가 홀수(False)인지 짝수(True)인지 판별해주는 함수 is_odd를 작성해보자 
print("퀴즈 1번")
def is_odd(value):
    if value % 2 == 0:
        print("짝수입니다")
        return True
    else:
        print("홀수입니다")
        return False
    
input_data = int(input("홀짝 분별을 위한 수를 입력하세요 : "))
is_odd(input_data)
print()
print()

# 퀴즈2) 입력으로 들어오는 모든 수의 평균값을 계산하는 함수를 작성해 보자 (단 입력으로 들어오는 수의 개수는 정해져 있지 않다)
print("퀴즈 2번")
def aver(*nums):
    result = 0
    for num in nums:
        result += num
    return result / len(nums)

print(f"avg = {aver(3,4,5,6,7,8)}")
print()
print()

# 퀴즈3) 새로운 계좌 개설하기 함수정의1 
# (매개변수X, 리턴값X 함수 (open_account(), "새로운 계좌가 생성되었습니다." 출력하기)
# 임금 함수2(매개변수O, 리턴값O 입금함수2, deposit(현재잔액, 입금액), 입금액을 더한 잔액을 리턴해준다.)
# 출금 함수3(매개변수O, 리턴값O 출금함수3, withdraw(현재잔액, 출금액), 출금액을 뺸 잔액을 리턴해준다.)
# 저녁 출금함수(매개변수O, 리턴값O 저녁출금함수4, withdraw_night(현재잔액, 출금액), 수수료는 100원 고정, 수수료까지 뺀 잔액과 수수료도 같이 리턴한다)
print("퀴즈 3번")
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, in_depo):
    return balance + in_depo

def withdraw(balance, out_with):
    if balance < out_with:
        print("잔액이 부족하여 출금할 수 없습니다.")
        print(f"현재잔액: {balance}, 출금요청 금액: {out_with}")
        return balance
    else:
        return balance - out_with

def withdraw_night(balance, out_with):
    if balance < out_with:
        print("잔액이 부족하여 출금할 수 없습니다.")
        print(f"현재잔액: {balance},  출금요청 금액: {out_with}")
        return balance
    else:
        comm = 100
        return balance - out_with - comm , comm

open_account()
now_charge = 100000
print(f"현재잔액: {now_charge}원")
now_charge = deposit(now_charge, 2000)
print(f"현재잔액: {now_charge}원")

now_charge = withdraw(now_charge, 150000)
print(f"현재잔액: {now_charge}원")

now_charge, comm = withdraw_night(now_charge, 3000)
print(f"현재잔액: {now_charge}원, 저녁 출금 수수료:{comm}")
print()
print()

# 가변 매개변수 
def profile(name, age, *main_lang):
    print(f"이름: {name}\t나이: {age}\t사용언어: {main_lang}")

profile("유재석", 40, "파이썬")
profile("박명수", 50, "C++")
profile("정형돈", 30, "JAVA")
print()
print()

# ======================== 수업 내용 ========================

# 람다식 
add = lambda a,b : a+b
# 아래 함수와 동일함
# def add(a,b):
#    return a+b
result = add(4,5)
print(result)

myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](3,4))
print(myList[1](3,4))
print()
print()




# 파일 처리 (열기, 읽기, 쓰기)

# 파일 열기(없으면 생성)
# f = open("newfile.txt","w",encoding="UTF-8")
# f = open("newfile.txt","a",encoding="UTF-8")
# f = open("newfile.txt","r",encoding="UTF-8")

# 파일 쓰기 
# f.write("파이썬은 쉽습니다\n")
# f.write("파이썬은 재미있습니다\n")

# 파일 읽기 (readline(): 한줄 읽기)
# line = f.readline()
# print(line)

# 파일 여러줄 읽기 (readline() 이용)
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)

# 파일 여러줄 읽기 (readlines() 이용)
# lines = f.readlines()
# for line in lines:
#     print(line)

# 파일 통째로 읽기 (read() 이용)
# lines = f.read()
# print(lines)


# # 파일 닫기
# f.close()

# with 키워드 
# with open("newfile2.txt", "a", encoding="UTF-8") as f:
#     for i in range(2, 11):
#        f.write(f"{i}번째 줄입니다. Life is too short, you need python\n")

# with open("newfile2.txt", "r", encoding="UTF-8") as f:
#     line = f.read()
#     print(line)

# 랜덤하게 1000명의 키와 몸무게 만들기

# 랜덤 숫자 임포트 
import random
# 간단한 한글 리스트 만듬 
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기로 엶 
with open("info.txt", "w", encoding="UTF-8") as file:
    for i in range(1000):
        # 랜덤 값으로 변수 생성 
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 작성 
        file.write(f"{name}, {weight}, {height}\n")

# 파일을 읽기로 엶
with open("info.txt", "r", encoding="UTF-8") as file:
    for line in file:
        # 변수를 선언함 
        (name, weight, height) = line.strip().split(", ")

        # 데이터 이상 유무 확인 
        if (not name) or (not weight) or (not height):
            continue
        
        # 결과를 계산함 
        bmi = int(weight) / int(weight) * int(height)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        # 출력부분 
        print('\n'.join([f"이름:{name}", 
                         f"몸무게:{weight}", 
                         f"키:{weight}", 
                         f"BMI:{bmi}", 
                         f"결과:{result}"]))
        print()