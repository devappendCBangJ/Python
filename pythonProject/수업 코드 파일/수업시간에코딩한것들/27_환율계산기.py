import urllib.request as req
from bs4 import BeautifulSoup

print("=== 메 뉴 ===")
print("1. 미국")
print("2. 일본")
print("3. 유럽")
print("4. 중국")
print("============")
menu = int(input("선택 >> "))
unit = ["달러", "엔", "유로", "위안"]
money = int(input("금액 입력 (단위 : {}) >> ".format(unit[menu-1])))
if menu == 2: # 일본을 선택했다면?
    money = money / 100
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
# price = soup.select("ul#exchangeList span.value")
price = soup.select("span.value")
price = float(price[menu-1].string.replace(",", ""))
print(price * money)
