# <문자열 대체 함수>
# .replace("특정 문자열", "새로운 문자열") : 특정 문자열 >> 새로운 문자열로 변경

import urllib.request as req
from bs4 import BeautifulSoup

print("=== 메 뉴 ===")
print("1. 미국")
print("2. 일본")
print("3. 유럽")
print("4. 중국")
print("=============")
menu = int(input("선택 >> "))
unit = ["달러", "엔", "유로", "위안"]
money = int(input("금액 입력 (단위 : {}) >> ".format(unit[menu - 1])))

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
price = soup.select("ul#exchangeList span.value")
# price = soup.select("div.market1 span.value") #위와 같음
# price = soup.select("ul.data_list span.value) #위와 같음

price = float(price[menu - 1].string.replace(",", ""))
# - 네이버에서 제공하는 환율은 문자형태에서 ","를 포함한 채로 제공됨. 이를 없애서 숫자형으로 바꿔주기 위해 replace() 함수 사용
# - 네이버에서 제공하는 환율은 소수점을 제공하기 때문에 정수형인 int가 아닌 실수형인 float 함수를 사용

if menu == 2: #사용자가 일본 menu를 선택했다면
    price = price / 100

print(price * money)