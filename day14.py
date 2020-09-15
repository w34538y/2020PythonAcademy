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


# 크롬 브라우저 제어하기 
# 브라우저를 사용하여 검색어를 전달하여 검색 결과 확인

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = "https://www.google.com/search?q="
plus_url = input("검색어를 입력하세요 : ")
url = base_url + quote_plus(plus_url)
print(url)

# 파이썬에서 크롬 브라우저를 실행시키기 
driver = webdriver.Chrome('/Users/shin/Desktop/폴더/강의 자료/20-여름 계절학기 강의자료/파이썬/pyfiles/chromedriver')
driver.get(url)

# 구글로 열린 웹페이지 정보를 가져옴 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

r = soup.select(".r") # class = r
for i in r:
    print(i.select_one(".LC20lb.DKV0Md").text)
    print(i.select_one(".iUh30.bc.tjvcx").text)
    print(i.a.attrs["href"])
    print()

driver.close()