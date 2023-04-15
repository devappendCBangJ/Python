import urllib.request as req
from bs4 import BeautifulSoup
import requests

# cgv 무비 차트 크롤링
code = req.urlopen("http://www.cgv.co.kr/movies/")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("div.sect-movie-chart strong.title")
poster_image = soup.select("span.thumb-image > img")

# 라인 단톡방 알림
api_key = "QAIxdX2oPirksnErNLO33QYQHPIUkyFUHghtk7N9nIn"
h = {"Authorization": "Bearer {}".format(api_key)}

for i in range(len(title)):
    d = {"message": "{}위 : {}".format(i+1, title[i].string),
         "imageThumbnail" : poster_image[i].attrs["src"],
         "imageFullsize" : poster_image[i].attrs["src"]}
    requests.post("https://notify-api.line.me/api/notify", headers=h, data=d)