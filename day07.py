# 7월 21일 강의
# 반복문 복습 예제 
# 당신은 택시 기사입니다 
# 50명과 매칭 기회가 있을 때 , 총 탑승 승객수를 구하는 프로그램을 작성하시오 
# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다 
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다 

# 출력문 예제) 0, 또는 비워두기 
# [0] 1반쩨 손님 (소요시간 : 15분)
# [] 2번째 손님 (소요시간 : 50분)
# ...
# [] 50번째 손님 (소요시간 : 15분)

# 총 탑승 승객 : 2분 

#########################################

from random import *
cnt = 0 # 총 탑승 승객 수 
for i in range(1, 51):
    time = randrange(5, 51) # 5분에서 50분 소요시간 
    if 5 <= time <= 15: # 매칭성공 
        print(f"[O] {i}번쩨 손님(소요시간 : {time}분)")
        cnt += 1
    else: # 매칭실패
        print(f"[ ] {i}번쩨 손님(소요시간 : {time}분)")
print(f"총 탑승 승객 : {cnt}명")
print()
print()

# 컴퓨터와 숫자 맞추기 게임 
# 1~30 사이에 있는 임의의 수를 컴퓨터는 하나 생성 
# 영원히 반복(사용자가 맞출때까지 무한 반복함)
# 입력받은 값을 비교할 수 있도록 정수로 바꿈 
# 사용자가 추측한 값과 임의의 수가 같아야 함 
# 정답을 맞히면 break로 while 반복 블록을 빠져 나감 

#출력 결과 
# 맞혀보세요? 15
# 너무 커요 
# 맞혀보세요? 10 
# 너무 작아요 
# 맞혀보세요? 14
# 정답 

# from random import *

# answer_set = randint(1, 30)
# print("제가 생각한 숫자가 무엇일까요?")


# while True:
#     answer_input = int(input("맞혀보세요?"))
#     if answer_input == answer_set:
#         print("정답!")
#         break
#     elif answer_input >= answer_set:
#         print("너무 커요")
#     elif answer_input <= answer_set:
#         print("너무 작아요")


def print_3_times(): # 사용자 정의 함수를 정의 
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
print()
print()


# def print_n_times(value, n): # 입출력이 없는 사용자 함수
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5) 
print()
print()

def sum(a, b): # 입출력이 있는 사용자 함수
    result = a + b
    return result

a = sum(3, 4)
print(a)
print()
print()

# 키워드 매개변수
def print_n_times(*value, n=2): # 입출력이 없는 사용자 함수
    for i in range(n):
        for values in value:
            print(values)

print_n_times("김대현", n=3)
print()
print()

# def multi_sum(*args): # 가변 매개변수 있고, 리턴값이 있는 함수 정의
#     result = 0
#     for i in args:
#         result += i
#     return result

# a = multi_sum(3,4,5,6)
# print(a)
print()
print()

def print_kwargs(**args): # 키워드 가변 매개변수 있고, 리턴값이 있는 함수 정의
    for k in args.keys():
        if k == "b":
            print(args[k])
            print(type(args))

a = print_kwargs(b = 30, c = 20)
print()
print()

def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print("0 to 100", sum_all(0, 100))
print("0 to 1000", sum_all(0, 1000))
print("50 to 100", sum_all(50, 100))
print("500 to 1000", sum_all(500, 1000))
print()
print()

def sum_all2(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output

a = sum_all2(0, 100, 10)
print("A: {0}".format(a))
print("B:", sum_all2(end=1000))
print(f"C: {sum_all2(end=100, step=2)}")
print()
print()

def sum_and_mul(a,b):
    return (a+b, a*b)

a = sum_and_mul(3, 5)
print(a)