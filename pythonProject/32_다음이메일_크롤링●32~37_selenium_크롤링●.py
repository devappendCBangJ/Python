#View > Tool Windows > Terminal에서 Terminal창에 pip install selenium 입력
#크롬 브라우저 우측 상단 ... >> 도움말 >> 크롬 정보 >> 버전 확인 >> 버전에 맞는 크롬 드라이버 검색 후 설치 >> pythonProject 폴더에 chromedriver.exe 파일 넣어주기

#<BeautifulSoup 사용 순서> 페이지 가상 가동
# 1. html코드 서버로부터 받아오기
# 2. html코드 이쁘게 정리하기
# 3. 원하는 요소 컴퓨터에게 알려주기 --> select() or select_one()

#<selenium 사용 순서> 페이지 직접 가동
# 0. 시간 모듈 불러오기 : import time
# 0. 셀레니움 모듈 불러오기 : from selenium import webdriver
# 0. 셀레니움 키보드 키 모듈 불러오기 : from selenium.webdriver.common.keys import Keys

# 1. 크롬 브라우저 실행 옵션 - 브라우저 창 닫은 채로 실행 : webdriver.ChromeOptions.add_argument("headless")
# - 브라우저 창 눈에 보이지 않음 & 시간 이득
# 1. 크롬 브라우저 실행 옵션 - 브라우저 창 열리면서 실행 :
# - 브라우저 창 눈에 보임 & 시간 손해
# 2. 크롬 드라이버 실행 및 옵션 설정 : browser = webdriver.Chrome("크롬 드라이버 파일 위치/크롬 드라이버 파일명.exe", options=webdriver.ChromeOptions.add_argument("headless"))
# 3. 웹 페이지로 이동 : browser.get("웹 페이지 주소")

# <웹에서 특정 요소 소스코드 파악하는 방법>
# 1way. 필요한 부분 오른쪽 마우스 클릭 >> 검사
# 2way. F12 >> ctrl+shift+c >> 필요한 부분 클릭
# 3-1. 원하는 요소 가져오기 전, 해당 요소 Ctrl + F를 통해 개수 / 정확도 파악
# 3-2. 속성값에 공백이 포함되어있을 때 : .로 치환해서 표현
# <css선택자> 기호를 이용하여 내가 원하는 요소 컴퓨터에게 전달
# 1) "." : class속성명
# 2) "#" : id속성명
# 대부분의 사이트에서 이미지 관련 tag명 : img
# 대부분의 사이트에서 id와 pw 관련 tag명 : input
# 1) ">" : 부모-자손 관계
# 2) " " : 조부모-후손 관계
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#4. 원하는 요소 컴퓨터에게 알려주기 --> brower.find_elements_by_css_selector("원하는 요소") or find_element_by_css_selector("원하는 요소")
# browser.find_element_by_css_selector("원하는 요소") : css선택자에 해당하는 요소에서 가장 위 1개
# browser.find_elements_by_css_selector("원하는 요소") : css선택자에 해당하는 요소 list자료형으로 전부
# browser.find_element_by_name("name속성명에 해당하는 속성값") : name 속성명에 해당하는 속성값 불러오기
# browser.find_element_by_css_selector("원하는 요소").get_attribute("원하는 속성명") : 속성값 불러오기
# browser.find_element_by_css_selector("원하는 요소").send_keys("입력할 문자열") : 문자열 입력
# browser.find_element_by_css_selector("원하는 요소").click() : 버튼 클릭

#5. 웹 페이지 넘어갈 때 시간 지연 - 파이썬 실행 속도가 크롬 불러오는 시간보다 빠르기 때문 : time.sleep(sec)
#5. 현재 웹 페이지 주소 추출 : browser.current_url

#6. 크롬 브라우저 종료 : browser.close()

# 태그명 속성명 속성값 내용
# BeautifulSoup : ".string"
# Selenium : ".text" 암기 하십쇼

#<selenium 장점>
# 1. 범용성 : 모든 사이트 크롤링 가능
# 2. 편리성 : 코드 작성 편리

#<selenium 단점>
# 1. 속도 : BeautifulSoup의 10배 정도 느림
# 2. 실험 필요 : 장소에 따라, 컴퓨터에 따라 사이트에서 로딩하는 속도가 다르므로 time.sleep()가 달라져야함

#<selenium을 꼭 써야하는 상황>
# 1. 로그인이 필요할 때
# 2. 웹페이지가 동적일 때(마우스 스크롤이 필요한 경우 등등...)

#<웹에서 특정 요소 소스코드 파악하는 방법>
# 1. 필요한 부분 오른쪽 마우스 클릭 >> 검사
# 2. F12 >> ctrl+shift+c >> 필요한 부분 클릭 (우클릭 막아놓은 사이트에서 유용)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

from selenium import webdriver #selenium 모듈의 기능 : 브라우저 창을 파이썬 명령어로 제어
import time

option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome("./chromedriver.exe", options=option)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

id = browser.find_element_by_css_selector("input#id")
id.send_keys("★daum_id★")
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("★daum_password★")
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(1)
#파이썬의 실행속도가 크롬 브라우저 실행 속도보다 빠르므로 조금 기다려줌

browser.get("https://mail.daum.net/")
time.sleep(1)
title = browser.find_elements_by_css_selector("strong.tit_subject") #리스트 자료형으로 반환됨
for i in title:
    print(i.text)
browser.close()


