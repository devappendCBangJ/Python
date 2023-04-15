import urllib.request as req
from bs4 import BeautifulSoup

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
# price = soup.select("ul#exchangeList span.value")
price = soup.select("span.value")
cnt = 0
for i in price:
    print(i.string)
    cnt += 1
    if cnt == 4:
        break
