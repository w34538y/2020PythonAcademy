from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    url = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(url, "html.parser")
    output = ""

    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력함 
        output += "<h3>{0}</h3>".format(location.select_one("city").text)
        output += "날씨:{0}</br>".format(location.select_one("wf").text)
        output += "최저/최고 기온 :{0} / {1}".format(location.select_one("tmn").text, location.select_one("tmx").text)
        output += "<hr/>"

    return output

# export FLASK_APP=FlaskTest
# flask run 해줘야 작동함 