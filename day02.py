print("# 기본적인 연산")
# 한줄 주석 
# 여러줄 주석 
''' 
여
러
줄
주
석
'''
print("+", 4, "=", 15 + 4)
print("/", 4, "=", 15 / 4)
print("%", 4, "=", 15 % 4)
print("//", 4, "=", 15 // 4)

# 3462를 17로 나누었을 때의 몫과 나머지를 구하시오. 
# 3462를 17로 나누었을 때의 
# 몫 : 
# 나머지 :
print("몫 : ", 3462 // 17)
print("나머지 : ", 3462 % 17)

print(2+2-2*2/2*2)
print(2-2+2*2/2+2)

a = "Life is too short, You need Python"
print(a[:4])

# You 단어 추출하기 
print(a[19:22])
# need python 단어 추출해서 출력하기 
print(a[23:])

a = "20151654신우진"
print(a[:8])
print(a[8:])

a = "801011-1068214"
print(a[7:8])


print()

print()

print()

print()

list_a = [273, 32, 103, "문자열", True, False]
# 리스트 0번째 인덱스에 해당하는 요소 추출
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print(type(list_a))
print(list_a[4:])
print()
print()

students = ["홍길동", "김갑자", "이길순", "장영웅", "박석기", "송민규"]
students2 = [100, 50, 70, 80, 90, 60]
# 전체 학생 명단
print(students)

# 학생 개인이름 
print("인덱스 0: ", students[0])
print("인덱스 1: ", students[1])
print("인덱스 2: ", students[2])
print("인덱스 3: ", students[3])

# 전체 학생수 
print("전체 학생수 : ", len(students))
print(students + students2)
print(students2 * 2)
print()

# 해당 리스트 인덱스의 요소를 변경하기
students[3] = "최은서"
print(students)

# 해당 인덱스 요소를 삭제하기 
del students[5]
print(students)

# 인덱스 전체 요소 삭제하기 
del students[0:]
print(students)

print()
print()
print()

students = ["홍길동", "김갑자", "이길순", "장영웅", "박석기", "송민규"]

# 요소를 추가 하는 함수 append()
students.append("유재석")
print(students)

# 요소를 삭제 하는 함수 pop()
students.pop()
print(students)

# 2번 요소를 삭제하는 함수 pop()
students.pop(2)
print(students)

# 리스트에 요소 삽입하는 함수 insert()
students.insert(3, "박명수")
print(students)

print()
print()
print()
print()
print()
print()

students = ["홍길동", "김갑자", "이길순", "장영웅", "박석기", "송민규"]
print(students)

# 요소 삭제 함수 remove()
students.remove("박석기")
print(students)

# 리스트 요소 정렬 sort()
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)
print()

# 리스트 확장 extend()
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)

# 리스트에 포함된 요소 x의 개수 세기 count()
print(students.count("송민규"))

print()
print()
print()

# 튜플
t1 = (1, 2, "a", "b")
t2 = (3, 4)
print(t1 + t2)
# 슬라이싱
print(t1[1:])
# index 함수 (검색)
print(t1.index("a"))
print(t1.count("b"))

print()
print()
print()

# 딕셔너리 
dic = {10: "강보경", 20: "조병수", 30 : "송근호", 40: "이대은"}
print(dic)
# 딕셔너리 쌍 추가하기 
dic[50] = "최은서"
print(dic)
# 딕셔너리 값 삭제하기 
del dic[10]
print(dic)
# key를 통해서 value를 얻기
print(dic[20])
# key를 중복할 경우 마지막에 입력된 데이터만 남음
dic[20] = "최은서"
print(dic)

dic2 = {"name" : "변창우", "name2" : "김민성"}
# key리스트 만들기 (keys())
print(dic2.keys())
# value 리스트 만들기 (values())
print(dic2.values())
# key와 value 쌍을 확인 (items())
print(dic2.items())
# key, value 쌍을 모두 지우기 (clear())
dic2.clear()
print(dic2)
# key를 통해서 value를 얻기 (get())
dic2 = {"name" : "변창우", "name2" : "김민성"}
print(dic2.get("name"))
print(dic2.get("name2"))

print(dic2["name"])
print(dic2["name2"])
