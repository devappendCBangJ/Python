#View >> Tool Windows >> Terminal에서 Terminal창 >> pip install openpyxl bs4 pillow 입력

#<BeautifulSoup 사용 순서>
# 0. 브라우저 불러오기 모듈 : import urllib.request as req
# 0. 소스 코드 정리 모듈 : from bs4 import BeautifulSoup
# 0. https사이트 크롤링 인증요청 모듈 : import ssl

# 1. html코드 서버로부터 받아오기 : urllib.request.urlopen("서버 주소")
# 1. 나의 정보를 서버에 보냄 + html코드 서버로부터 받아오기 : urllib.request.Request("https://www.melon.com/chart/", headers = {"User-Agent":"Mozilla/5.0"}
    # - 서버가 크롤링 봇 or 해커라고 의심 >> 나의 정보 보내서 접속 허락 받음
# 1. html코드 서버로부터 한국어로 받아오기 : headers = req.Request("https://www.op.gg/champion/statistics", headers={"Accept-Language":"ko-KR"})
# 1. https html코드 서버로부터 받아오기 : context = ssl._create_unverified_context()
    # urllib.request.urlopen("서버 주소", context=context)

    # <웹에서 특정 요소 소스코드 파악하는 방법>
    # 1way. 필요한 부분 오른쪽 마우스 클릭 >> 검사
    # 2way. F12 >> ctrl+shift+c >> 필요한 부분 클릭
# 2. html코드 이쁘게 정리하기 : BeautifulSoup(html코드, "html.parser")
# 3. 원하는 요소 컴퓨터에게 알려주기 & 해당 요소 list자료형으로 전부 가져오기 : BeautifulSoup(html코드, "html.parser").select("원하는 요소")
# 3. 원하는 요소 컴퓨터에게 알려주기 & 해당 요소 1개만 가져오기 : BeautifulSoup(html코드, "html.parser").select_one("원하는 요소")
# 3-1. 원하는 요소 가져오기 전, 해당 요소 Ctrl + F를 통해 개수 / 정확도 파악
# 3-2. 속성값에 공백이 포함되어있을 때 : .로 치환해서 표현
    # <css선택자> 기호를 이용하여 내가 원하는 요소 컴퓨터에게 전달
    # 1) "." : class속성명
    # 2) "#" : id속성명
    # 대부분의 사이트에서 이미지 관련 코드명 : img
    # 1) ">" : 부모-자손 관계
    # 2) " " : 조부모-후손 관계
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # select_one("원하는 요소") : css선택자에 해당하는 요소에서 가장 위 1개
    # select("원하는 요소") : css선택자에 해당하는 요소 list자료형으로 전부
    # 태그명:nth-child(?) : 같은 태그명인 자손이 있을 때, ?번째에 있는 자손을 불러옴

    # 해당 요소에서 속성값 가져오기 : BeautifulSoup(html코드, "html.parser").select_one("원하는 요소").attrs["속성명"]

    # <텍스트 추출>
    # BeautifulSoup 텍스트 추출 : .text 사용
    # 요소 안에 또다른 요소가 들어있을 경우 텍스트 추출 : none으로 출력되므로 .string이 아닌 .text 사용
    # 문자열 양 끝 공백과 \n 제거 : .text.strip().replace("   ","")
    
    # 태그명 속성명 속성값 내용
# 4. 출력 by for문 / 그냥 추출
    #.string : BeautifulSoup에서 요소의 내용만 추출


# <문자열 대체 함수>
# .replace("특정 문자열", "새로운 문자열") : 특정 문자열 >> 새로운 문자열로 변경


import urllib.request as req # 브라우저 불러오기 모듈
from bs4 import BeautifulSoup # 소스코드 정리 묘듈

code = req.urlopen("http://www.cgv.co.kr/movies/") # 1. html코드 서버로부터 받아오기
# print(code.read()) #확인용 코드
soup = BeautifulSoup(code, "html.parser") # 2. html코드 이쁘게 정리하기
# print(soup) #확인용 코드

title = soup.select("div.sect-movie-chart strong.title") # 3. 원하는 요소 컴퓨터에게 알려주기

#title = soup.select("strong.title")
#title = soup.select_one("strong.title") #태그명이 strong이고, 속성명이 class, 속성값이 title인 요소 1개만 가져와
#title = soup.select_one("div#movie") #태그명이 div이고, 속성명이 id, 속성값이 movie인 요소 1개만 가져와
#title = soup.select_one("a > strong.title") #태그명이 a인 요소의 자손이고 strong.title인 요소 1개만 가져와
#title = soup.select_one("div.box-contents strong.title") #div.box-contents인 요소의 후손이고, strong.title인 요소 1개만 가져와

for i in title:
    print(i.string)
# print(title) #확인용 코드