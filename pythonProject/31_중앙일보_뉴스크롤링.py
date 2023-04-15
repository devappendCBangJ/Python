# <문자열 수정 함수>
# 문자열 양 끝 공백과 \n 제거 : .strip()
# 문자열 대체 : .replace("대체할 문자", "새로운 문자")

# 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용

# 개행 : print()

import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par

keyword = input("키워드를 입력하세요 >> ")
encoded = par.quote(keyword)
page_num = 1
while True:
    code = req.urlopen("https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded))
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: #끝 페이지까지 크롤링을 완료해서 title의 원소개수가 0개가 된다면
        break
    for i in title:
        print("제목 :", i.text)
        # 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용
        #i.text와 title[i].text는 같음
        print("링크 :", i.attrs["href"])
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        print(content.text.strip().replace("   ",""))
        # 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용
        print() #개행
    page_num += 1 #페이지가 넘어가면 url주소가 아예 바뀌니까
    # while안에 정의한 url 주소와 같은 곳에 두기 위해 for문 밖으로 빼둠