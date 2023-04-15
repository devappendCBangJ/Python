# 사이트 : 동아일보 아카이브
# ID : talingpython
# PW : 탈잉파이썬2

#<BeautifulSoup 로그인 포스트 데이터>
# f12 >> Network >> preserve log 체크 >> All >> 이 상태에서 로그인 >> 이 때 표시되는 trans_exe.php 확인
# [General]
# get방식 : 서버 요청 시, 요청 메시지를 함께 실어 보낸다... 간편하지만, 보안에 취약함 ex) 보안이 필요하지 않은 모든 것들에 주로 사용
# POST방식 : 요청 메시지를 일종의 택배 상자에 실어 보낸다... 보안에 강함 ex) 로그인에 사용
# [Response Headers] : 서버가 응답 시 사용자에게 제공한 데이터
# [Request Headers] : 사용자가 요청 시 서버에게 제공한 데이터

#<elements에서 본문으로 넘어가는 url 주소를 알 수 없을 때 - Network에서 본문으로 넘어가는 url 주소 따기>
# f12 >> Network >> preserve log 체크 >> All >> 이 상태에서 본문으로 진입하는 기사 버튼 클릭 >> Headers >> 이 때 표시되는 파일 확인 후 url 이용

# <BeautifulSoup 로그인 순서>
# 0. import requests
# 0. 소스 코드 정리 모듈 : from bs4 import BeautifulSoup

# 1. 세션 만들기 - 서버 & 컴퓨터 사이 연결고리 : requests.session()
# 2. 포스트 요청 - 서버에 필요한 데이터 제공 및 데이터 요청 :
    # general / request_headers / form_data 값을 딕셔너리 형태로 서버에 제공 및 포스트 요청
# form_data = {
# "idsave_value" : "",
# "errorChk" : "",
# "gourl" : "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19970701%26mode%3D19970701%2F0002891658%2F1", #로그인 화면 이후 넘어갈 url
# "bid" : "talingpython", #입력할 ID
# "bpw" : "xkfdldvkdlTjs2"} #입력할 PW
# request_headers = {'referer' : 'https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19970701%26mode%3D19970701%252F0002891658%252F1'}
# requests.session.post("https://secure.donga.com/membership/trans_exe.php", headers=request_headers, data = form_data)
# 3. 세션 연결 & 코드 가져오기 & 요소 딕셔너리 형태로 가져오기 : BeautifulSoup(requests.session.get("웹 주소").text, "html.parser").select("요소")
# 3. 세션 연결 & 코드 가져오기 & 요소 하나만 가져오기 : BeautifulSoup(requests.session.get("웹 주소").text, "html.parser").select_one("요소")
    # get()함수 : code.text
    # urlopen()함수 : 그냥 code


import requests
from bs4 import BeautifulSoup

#크롤링 권한 얻기
sess = requests.session()
#f12 >> Network >> preserve log 체크 >> All 체크 >> 이 상태에서 로그인 >> 이 때 표시되는 trans_exe.php >> form_data 읽기
form_data = {
"idsave_value" : "",
"errorChk" : "",
"gourl" : "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19970701%26mode%3D19970701%2F0002891658%2F1", #로그인 화면 이후 넘어갈 url
"bid" : "talingpython", #입력할 ID
"bpw" : "xkfdldvkdlTjs2"} #입력할 PW
request_headers = {'referer' : 'https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19970701%26mode%3D19970701%252F0002891658%252F1'}
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=request_headers, data = form_data) #포스트 요청 : 서버에 필요한 데이터 제공, 서버에게 데이터 요청

#크롤링
code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19970701&mode=19970701/0002891658/1")
soup = BeautifulSoup(code.text, "html.parser")
title = soup.select("ul.news_list > li > a")
# req.urlopen()함수를 쓰면 위에서 사이트와 연결고리를 만들어 놨던 것이 의미가 없어짐
for i in title:
    print(i.string)
    # print(i.attrs["onclick"].replace("javascript:getNewsArticle('19970701/", "").replace("/1'); return false;", "")) #확인용 코드

    content_num = i.attrs["onclick"].replace("javascript:getNewsArticle('19970701/", "").replace("/1'); return false;", "")
    #content_url = "https: // www.donga.com / archive / newslibrary / view?idx = 19970701 % 2F" + content_num + "% 2F1" #이렇게 하면 왜 안됨?????????
    content_url = "https://www.donga.com/archive/newslibrary/view?idx=19970701%2F{}%2F1".format(content_num)

    code = sess.get(content_url)
    soup = BeautifulSoup(code.text, "html.parser")
    content = soup.select_one("div.article_txt")

    print(content.text.strip())
    # print(content.string) #요소 안에 요소가 존재하면 .string 사용 시 none이 출력되므로 .text 사용해야함
    print()

    # 본문 주소 찾기 과정
    # url = "https://www.donga.com/archive/newslibrary/view?idx=19970701%2F0002891657%2F1" #주소 변화에 규칙이 없어서 for문을 돌릴 수 없음
    # Elements에서 본문 주소를 찾을 수 없음 >> Network에서 본문 주소 규칙성을 찾지 못함 >>
    # >> Network에 표시된 주소와 Elements에 표시된 주소 사이의 연관성 파악(Elements에서 Network 주소 조합에 사용되는 일부 주소를 가지고 있다는 것 확인)
    # >> replace 함수를 이용해서 본문이 달라짐에 따라서 변화하는 url 주소 부분만 이용