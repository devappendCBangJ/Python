import urllib.request as req
from bs4 import BeautifulSoup

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
price = soup.select("ul#exchangeList span.value")
# price = soup.select("div.market1 span.value") #위와 같음
# price = soup.select("ul.data_list span.value) #위와 같음

for i in price: #.string은 html 요소를 들고 있는 변수 뒤에만 올 수 있다. 그래서 for문 돌려야함
    print(i.string)

# [other way]
# cnt = 0
# for i in price:
#     print(i.string)
#     cnt += 1
#     if cnt == 4: #여기서 break 안하면 오류 뜨나? price 원소 개수가 고갈되면 자동으로 끝나는 것 아닌가??????????????????????????????
#         break