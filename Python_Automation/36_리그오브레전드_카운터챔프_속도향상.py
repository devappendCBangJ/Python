# 해당 요소에서 속성값 가져오기 : BeautifulSoup(html코드, "html.parser").select_one("원하는 요소").attrs["속성명"]

import urllib.request as req
from bs4 import BeautifulSoup

your_champ = input("상대가 뽑은 챔프 입력 >> ")

# 한글 웹 사이트 요청
headers = req.Request("https://www.op.gg/champion/statistics", headers={"Accept-Language":"ko-KR"}) #op.gg에서 기본적으로 영어 형태의 웹페이지를 제공함
code = req.urlopen(headers)

# 지정한 챔프 탭 클릭
soup = BeautifulSoup(code, "html.parser")
champ_list = soup.select("div.champion-index__champion-list > div")
#BeautifulSoup를 이용해서 새로운 url로 접속해야 하므로 그것을 따올 수 있는 규칙을 찾아내야함
#챔피언에 해당되는 속성값이 전부 달라서 그 부모를 이용하고, 자손의 태그명까지만 불러오는 규칙으로 불러올 수 있음
for i in champ_list:
    # if i.string == your_champ: #챔피언 명이 요소로 표시되어 있지 않으므로, 이렇게 하면 안되고 속성값을 불러와서 비교해줘야한다
    # print(i.string) #확인용 코드
    if i.attrs["data-champion-name"] == your_champ: #챔피언 명이 요소로 표시되어 있지 않으므로, 속성값을 불러와서 비교
        a = i.select_one("a") #주어진 champ_list가 품고 있는 요소들 중에서 태그명이 a인 요소를 찾는다
        #a = i.select_one("div.champion-index__champion-list > div > a") #위와 똑같음
        champ_url = "https://www.op.gg" + a.attrs["href"] 
        #href에서 /champion/garen/statistics 밖에 출력되지 않으므로 앞에 생략된 url을 수동으로 붙여줌
        break
# print(champ_url) #확인용 코드

# 지정한 챔프의 카운터 탭 클릭
headers = req.Request(champ_url, headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
counter_tab = soup.select_one("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a")
counter_url = "http://www.op.gg" + counter_tab.attrs["href"]

# 카운터 챔프 리스트 크롤링
headers = req.Request(counter_url, headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
counter_champ_list = soup.select("div.champion-matchup-list__champion span:nth-child(2)")
num = 1
for i in counter_champ_list:
    print(num, ". ", i.string)
    num += 1
    
#어차피 코드는 순서대로 진행되니까 headers, code, soup에 넣는 값을 바꿔줘도 됨