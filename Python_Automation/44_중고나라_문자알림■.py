# 외부 모듈 자동 설치 : 설치되지 않은 모듈에 커서 >> Alt + Enter + Enter
# twilio.com >> 회원가입 >> 우측 상단 DOCS >> quickstart >> Programmable SMS Quickstart Python 예제 복붙
# >> 예제 수정 (trial number 발급 후 복붙 & account sid 복붙 & auth token 복붙)


from selenium import webdriver
import time
import os
from twilio.rest import Client

# 브라우저 열기
browser = webdriver.Chrome("./chromedriver")
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

# 로그인
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)

# 카페 열기
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)

# 중고나라 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # webdriver.Chrome("크롬 드라이버 위치/크롬 드라이버 파일명").switch_to.frame(webdriver.Chrome("크롬 드라이버 위치/크롬 드라이버 파일명").find_element_by_css_selector("프레임 요소")) : 프레임 전환 / 태그명 생력 가능
browser.find_element_by_css_selector("a#fldlink_rRa6_347").click()
time.sleep(3)

# 과거 게시물 제목이 저장되어있는 메모장 파일 불러오기
try: #오류 날 경우 대비 / 파일이 존재하면 파일 읽기
    f = open("./중고나라.txt", "r")
    ref = f.readlines() #딕셔너리 형태로 읽어들임
except: #파일이 존재하지 않으면, 파일 새로 생성
    f = open("./중고나라.txt", "w")
    ref = []

# 게시물 제목 크롤링
new_one = 0
title = browser.find_elements_by_css_selector("a.txt_item")
for i in title:
    if not (i.text + "\n") in ref: #크롤링한 제목이 최신의 글이라면? >> 메모장에 추가
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n") #여기서 개행문자 있게끔 저장시켰기 때문에, if문에서도 개행문자를 넣어서 찾아야함
        if "스마트폰" in i.text: # 관심있는 물건이라면?
            new_one += 1
f.close()

# 브라우저 닫기
browser.close()

# 문자 알림 API
if new_one >= 1: # 새로운 물건이 올라왔을 때 (작업 스케쥴러와 함께 사용하면 효과 굳)
    account_sid = "" # 삭제
    auth_token = "" # 삭제
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body = "{} 관련 글이 {}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6".format("스마트폰", new_one)),
                        from_='+19123333630',
                        to='+821025514969'
                     )
#아이디 생성 후 해보기