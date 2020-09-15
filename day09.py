# 7월 23일 강의 

# 파일 입출력 복습 
# with open("study.txt", "w", encoding="UTF-8") as study_file:
#   study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "w", encoding="UTF-8") as study_file:
#   data = study_file.read()
#   print(data)


# 퀴즈) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다 
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

# - X 주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오 
# 조건 : 파일명은 '1주차.txt', '2주차 txt'....와 같이 만듬 

# for i in range(1, 51):
#     with open("str(i)+주차","w", encoding="UTF-8") as report:
#         report.write(f"-{i}주차 주간 보고-")
#         report.write("\n부서: ")
#         report.write("\n이름: ")
#         report.write("\n업무: ")


# ======================== 수업 내용 ========================


# 예외처리
# try:
#     num_input = int(input("정수를 입력 >>>"))
#     print("원의 반지름 :", num_input)
#     print("원의 둘레 : ", 2 * 3.14 * num_input)
#     print("원의 넓이 : ", 3.14 * num_input * num_input)
# except:
#     print("잘못된 입력이 발생했습니다.")
#     # pass 키워드를 사용할 수도 있다.
# finally:
#     print("정상적으로 프로그램을 종료합니다")


# try:
#     print("나누기 전용 계산기 입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 입력입니다.")
# except ZeroDivisionError as err:
#     print("0으로 나눌 수 없습니다.")
#     print(err)


try:
    print("나누기 전용 계산기 입니다")
    num_list = []
    num_list.append(int(input("첫번째 숫자를 입력하세요: ")))
    num_list.append(int(input("두번째 숫자를 입력하세요: ")))
    num_list.append(num_list[0]/num_list[1])
    print(f"{num_list[0]} / {num_list[1]} = {num_list[2]}")
except ValueError:
    print("잘못된 입력입니다.")
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다.")
    print(err)

# 사용자 정의 에러 객체 
# class BigNumberError(Exception): # 내가 만든 에러 클래스로 Exception클래스를 상속받아 정의함
#     pass

# try:
#     print("나누기 전용 계산기 입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10: # 10이상이면
#         raise BigNumberError # 사용자 정의 에러 객체를 불러온다 
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 입력입니다.")
# except BigNumberError :
#     print("한자리 숫자만 입력하세요.")
# finally:
#     print("프로그램이 정상적으로 종료됐습니다.")

# 퀴즈) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다 
# 대기 손님의 치킨 요리 시간을 
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리 
# 출력 메세지 : "잘못된 값을 입력하였습니다"
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨양은 10마리로 한정 
# 치킨 소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료 
# 출력 메세지 : "재료가 소진되어 더 이상 주문이 불가능합니다"

# 실행 테스트에서 주문 갯수를 0을 입력, -1을 입력해보자 

chicken = 10
waiting = 1 # 홀안에는 현재 만석, 대기번호 1번부터 시작

class SoldOutError(Exception):
    pass

while True:
    try:
        print(f"남은 치킨: {chicken}")
        order = int(input("치킨 몇마리를 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0: # 조건1 처리문
            raise ValueError
        else:
            print(f"[대기번호 {waiting}] {order}마리 주문이 완료되었습니다 ")
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError:
        print("재료가 소진되어 더 이상 주문을 받지 않습니다")
        break # 프로그램 종료
