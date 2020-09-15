# 이미지 크롤링하기
import urllib.request
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
context = ssl._create_unverified_context()  # ssl에러 해결용 

# 1. 가져올 URL을 정하라 
fronturl = "https://www.google.com/search?q="
seturl = input("검색어를 입력하세요:")
endurl = "&newwindow=1&sxsrf=ALeKk02u88rClPFTS5oz4RvJBOW0gKu2-w:1596025068071&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZn_DZuPLqAhUNiZQKHYc9CI8Q_AUoAXoECBwQAw&biw=1378&bih=1090"
url = fronturl + quote_plus(seturl) + endurl

driver = webdriver.Chrome()
driver.get(url)
# 2. HTML을 읽어와라 
html = urllib.request.urlopen(url, context=context).read()

# 3. 분석하라(beautifulSoup 사용)
soup = BeautifulSoup(html, "html.parser")

# 4. 분석을 해서 분석한 결과중 원하는것만 가져와서 결과 확인하기 
img = soup.find_all(class_ = "rg_i Q4LuWd")
n = 1
for i in img:
    img_url = i["src"] # 이미지 주소를 모두 저장한 후 파일로 저장 
    with urllib.request.urlopen(img_url, context=context) as f:
        with open("./apple/"+ seturl + str(n)+".jpg","wb") as h: # 파일이름 : 딸기1.jpg, 딸기2.jpg
            img_sv = f.read()
            h.write(img_sv)
    n += 1
    print(f"{n}번째 이미지 다운로드중 {img_url}")

print("다운로드 완료")