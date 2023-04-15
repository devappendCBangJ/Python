import urllib.request as req
from bs4 import BeautifulSoup

your_champ = input("상대가 뽑은 챔프 입력 >> ")
headers = req.Request("https://www.op.gg/champion/statistics", headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
champ_list = soup.select("div.champion-index__champion-list > div")
for i in champ_list:
    if i.attrs["data-champion-name"] == your_champ:
        a = i.select_one("a")
        champ_url = "https://www.op.gg" + a.attrs["href"]
        break

headers = req.Request(champ_url, headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
counter_tab = soup.select_one("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a")

counter_url = "https://www.op.gg" + counter_tab.attrs["href"]
headers = req.Request(counter_url, headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
counter = soup.select("div.champion-matchup-list__champion > span:nth-child(2)")
for i in counter:
    print(i.string)









