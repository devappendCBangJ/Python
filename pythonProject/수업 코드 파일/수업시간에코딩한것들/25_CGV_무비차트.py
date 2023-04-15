import urllib.request as req
from bs4 import BeautifulSoup

# 서버로부터 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

title = soup.select("div.sect-movie-chart strong.title")
# print(title)
for i in title:
    print(i.string)