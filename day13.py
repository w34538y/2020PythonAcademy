# 퀴즈) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오 
# 조건 : 모듈파일명은 byme.py로 작성 

# 모듈 사용예제
# import byme
# byme.sign()

# 출력예제 
# 이 프로그램은 신우진에 의해 만들어졌습니다 
# 이메일 : w34538y@gmail.com

# import urllib

# from bs4 import BeautifulSoup
# import byme
# byme.sign()

# import inspect
# import random
# print(inspect.getfile(random))

# 외부 모듈 사용 
# 구글 크롤링 beautifulsoap 모듈 사용 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 1. 가져올 URL을 정하라 
# 2. HTML을 읽어와라 
# 3. 분석하라(beautifulSoup 사용)
# 4. 분석을 해서 분석한 결과중 원하는것만 가져와서 결과 확인하기 


# 기상청 날씨 가져오기
# # 모듈을 읽어 들임 
# from urllib import request
# from bs4 import BeautifulSoup

# # urloepn()함수로 기상청의 전국 날씨를 읽습니다 
# target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# # BeautifulSoup를 사용해 웹페이지를 분석함 
# soup = BeautifulSoup(target, "html.parser")

# # location 태그 찾기 
# for location in soup.select("location"):
#     # 내부의 city, wf, tmn, tmx 태그를 찾아 출력함 
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()


# 네이버 블로그 크롤링
# import urllib.request
# from urllib.parse import quote_plus
# from bs4 import BeautifulSoup
# import ssl

# context = ssl._create_unverified_context()
# # 1. 가져올 URL을 정하라 
# baseurl = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query="
# plusurl = input("검색어를 입력하세요:")
# url = baseurl + quote_plus(plusurl)

# # 2. HTML을 읽어와라 
# html = urllib.request.urlopen(url, context=context).read()

# # 3. 분석하라(beautifulSoup 사용)
# soup = BeautifulSoup(html, "html.parser")

# # 4. 분석을 해서 분석한 결과중 원하는것만 가져와서 결과 확인하기 
# title = soup.find_all(class_ = "sh_blog_title")
# # print(len(title))
# for i in title:
#     print(i.attrs["title"])
#     print(i.attrs["href"])


# 이미지 크롤링하기
import urllib.request
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()  # ssl에러 해결용 

# 1. 가져올 URL을 정하라 
baseurl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusurl = input("검색어를 입력하세요:")
url = baseurl + quote_plus(plusurl)

# 2. HTML을 읽어와라 
html = urllib.request.urlopen(url, context=context).read()

# 3. 분석하라(beautifulSoup 사용)
soup = BeautifulSoup(html, "html.parser")

# 4. 분석을 해서 분석한 결과중 원하는것만 가져와서 결과 확인하기 
img = soup.find_all(class_ = "_img")
n = 1
for i in img:
    img_url = i["data-source"] # 이미지 주소를 모두 저장한 후 파일로 저장 
    with urllib.request.urlopen(img_url, context=context) as f:
        with open("./apple/"+plusurl + str(n)+".jpg","wb") as h: # 파일이름 : 딸기1.jpg, 딸기2.jpg
            img_sv = f.read()
            h.write(img_sv)
    n += 1
    print(f"{n}번째 이미지 다운로드중 {img_url}")

print("다운로드 완료")