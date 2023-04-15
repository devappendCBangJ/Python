import urllib.request as req
from bs4 import BeautifulSoup #BeautifulSoup 모듈에는 로그인 기능이 없다

#그래프 그리기 초기 설정
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc #한글출력 설정
font_name = font_manager.FontProperties(fname="./batang.ttc").get_name()
plt.rc("font", family=font_name)

#그래프 그리기 초기 실정
plt.title("막대그래프(bar)")
plt.xlabel('숫자')
plt.ylabel('횟수')

x_data = []
for i in range(1,46): #range(1,46) : 1부터 45까지
    x_data.append(i)
# print(x_data)

y_data = []
for i in range(1,46):
    y_data.append(0)
# print(y_data)

data = 1
while True:
    code = req.urlopen("https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={}%ED%9A%8C%EB%A1%9C%EB%98%90".format(data))
    soup = BeautifulSoup(code, "html.parser")
    number = soup.select("div.num_box span")
    print([[data]], "회차 로또 번호 로딩중...")
    if(len(number)) == 0:
        break
    for i in number:
        if not "보너스번호" in i: #number에서 "보너스번호"라는 원소는 가져오지 않겠다
            #if i.find("보너스번호") == 0: #위와 같음
            # print(i.string)
            # print(number[i].string) #for문에서 i는 number라는 리스트형을 하나씩 가져오는데, 그렇게 되면 number[i]에서 i는 숫자가 아니라 리스트형의 원소임. 그래서 사용 불가
            y_data[int(i.string) - 1] += 1 #리스트형은 처음이 0번째이기 때문에 1부터 시작하는 i.string에서 1을 빼줘야 한다
            # print(y_data)
    data += 1

#그래프 그리기
# plt.bar(x_data,y_data) #bar(막대를 표시할 위치, 막대의 높이) #이걸로 그려도 되긴하지만, 다른 명령어를 이용하면 다른 형식으로도 그릴 수 있음
x = np.arange(45)
plt.bar(x, y_data) # x개수의 y데이터 그리기
plt.xticks(x, x_data) # x개수의 x데이터 그리기
plt.show()