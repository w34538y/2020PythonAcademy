# 7월 17일 강의
# 조건문 복습문제 
# 주머니에 돈이 있으면 택시를 타고, 카드가 있으면 택시를 타고, 주머니에 돈도 카드도 없으면 걸어가라 
pocket = ["paper", "cellphone"]
card = True 

if pocket == "money" or card == True:
    print("택시를 타세요")
else:
    print("걸어가세요")

print()
print()

list_a = [273, 32, 103, 57, 52]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])
print(list_a[4])
print()
for i in list_a:
    print(i)

print()
print()


dic = {"name" : "홍길동", "age" : 20}
print(dic["name"])
print(dic["age"])
print()
for i in dic:
    print(i, dic[i])

print()
print()

# 확인문제2
# 다음 반복문 내부에 if조건문의 조건식을 채워서 100이상의 숫자만 출력하게 만들어보세요 
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("100이상의 수 : ", number)
print()

# 짝수와 홀수로 구분하여 출력
print("# 짝수와 홀수로 구분하여 출력")
for number in numbers:
    if number % 2 == 0:
        print(f"{number}(은)는 짝수입니다.")
    else:
        print(f"{number}(은)는 홀수입니다.")
print()

# 값들의 자릿수(길이)를 출력 - len은 문자열을 읽어들임 숫자의 경우 len(str(변수명))으로 
print("# 값들의 자릿수(길이)를 출력")
for number in numbers:
    print(f"{number}(은)는 {len(str(number))}자리수 입니다.")
print()

# 리스트안의 리스트 
print("# 리스트안의 리스트 ")
list_of_list = [
    [1, 2, 3], 
    [4, 5, 6, 7], 
    [8, 9]
]

for i in list_of_list:
    for j in i:
        print(j)
print()

# 확인문제 5
print("# 배열의 요소값 갯수 확인해서 딕셔너리 출력")
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2,1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
print(counter)
print()

# 확인문제 6
# 딕셔너리 선언
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반복문을 사용함 
for key in character:
    if type(character[key]) is str:
        print(key,":",character[key])
    elif type(character[key]) is dict:
        for key2 in character[key]:
            print(key2,":", character[key][key2])
    elif type(character[key])is list:
        for key2 in character[key]:
            print(key,":",key2)
    else:
         print(key,":",character[key])
print()

# for문과 range함수를 사용하여 1부터 100까지의 합을 출력하시오 
sum = 0
for i in range (1, 101):
    sum += i
print(sum,"입니다")
print()

# for문과 range함수를 사용하여 구구단을 출력하시오 
for i in range(2, 10, 1):
    print(f"-----{i}단-----")
    for j in range(1, 10, 1):
        print(f"{i*j}", end=" ")
    print()
print()

# 5명의 학생이 시험을 보았는데 시험점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다 
# 합격인지 불합격인지 차례대로 검사해서 결과를 통보해주는 프로그램을 ㅏㄴ든다 
# 5명의 시험점수는 
std_list = [90, 225, 67, 45, 80]
for i in std_list:
    if i > 60:
        print(f"{i} : 합격입니다.")
    else:
        print(f"{i} : 불합격입니다.")
print()

# for문 연습예제 
starbucks = ["오상봉", "송근호", "신우진"]

for i in starbucks:
    print(f"{i}님, 커피가 준비되었습니다")