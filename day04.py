# 조건문 
# 날씨가 비가 많이 오면 우산을 챙기세요. 미세먼지가 많으면 마스크를 챙긴다.
weather = "비"
if weather == "비":
    print("우산을 챙기세요.")
    
print()
print()
# 조건문2
# 날씨가 비가 많이 오면 우산을 챙기고 미세먼지가 많으면 마스크를 챙긴다 
weather = input("현재 날씨는? : ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")
print()
print()

# 조건문3
# 기온에 따른 외출 조건을 알려주기
temp = int(input("현재 기온은? : "))
if 30<= temp : 
    print("날씨가 매우 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("날씨가 괜찮습니다.")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 춥습니다. 나가지 마세요")

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라는 문장을 조건문으로 만드시오 
pocket = ["money", "phone", "paper"]
if "money" in pocket:
    print("택시를 타세요")
else:
    print("걸어가세요.")

# 만약 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라는 문장을 조건문으로 만드시오 
if "card" not in pocket:
    print("걸어가세요")
else:
    print("버스를 타세요.")


# 확인문제

year = int(input("년도(yyyy)를 입력 : "))
year_cal = year % 12
if year_cal == 0:
    print("원숭이띠생입니다")
elif year_cal == 1:
    print("닭띠입니다")
elif year_cal == 2:
    print("개띠입니다")
elif year_cal == 3:
    print("돼지띠입니다")
elif year_cal == 4:
    print("쥐띠입니다")
elif year_cal == 5:
    print("소띠입니다")
elif year_cal == 6:
    print("범띠입니다")
elif year_cal == 7:
    print("토끼띠입니다")
elif year_cal == 8:
    print("용띠입니다")
elif year_cal == 9:
    print("뱀띠입니다")
elif year_cal == 10:
    print("말띠입니다")
else:
    print("양띠입니다")
    
print("프로그램 종료")