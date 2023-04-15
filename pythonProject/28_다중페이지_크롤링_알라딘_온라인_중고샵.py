#다중 페이지 크롤링 : 여러 페이지에 걸친 url을 메모장에 복사해봄(규칙을 찾아보자)

import urllib.request as req
from bs4 import BeautifulSoup
f = open("./알라딘중고샵.txt", "w")

page_num = 1
while True:
    url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("a.bo3 > b")
    price = soup.select("a.bo_used > b")
    if len(title) == 0: #끝 페이지까지 크롤링을 완료 시 탈출
        break
    for i in range(len(title)): #이전엔 for문 돌리면서 list자료형 원소를 통째로 가져왔음
    #이 예제는 title과 price 모두를 가져와야 하므로 list자료형의 index만 range로 불러온 후, 그것을 index로 사용
        print(title[i].string, price[i].string)
        f.write(title[i].string + ", " + price[i].string + "\n") #write() 함수는 ,로 이을 수가 없으므로 +를 이용해서 이어줌
    page_num += 1
f.close()