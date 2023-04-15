# send_keys()함수 사용 시 앞에 html요소가 필요

# <키보드 key 기능>
# PAGE_DOWN 키 : 원래 스크롤을 조금 내려주는 역할
# END 키 : 스크롤을 조금 내려주는 역할

# <오류 방지 명령어 try / except>
# try:
    # try 해 볼 명령어
# except:
#   try에서 되지 않을 경우 실행할 명령어

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#<드라이버로 브라우저 열기>
browser = webdriver.Chrome("./Chromedriver.exe")
browser.get("https://www.youtube.com/watch?v=6MyHdz_MW3Y")
time.sleep(4)

# #<맨 처음에 스크롤 조금 내려주기>
# browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
# time.sleep(3)

#<맨 처음에 스크롤 끝까지 내려주기>
browser.find_element_by_css_selector("html").send_keys(Keys.END)
time.sleep(3)
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

#<댓글 크롤링>
comments = browser.find_elements_by_css_selector("yt-formatted-string#content-text") #태그명을 쓰지 않고 "#content-text" 이런 식으로도 가능
cnt = 0
while True:
    try:
        print("●", comments[cnt].text)
    except:
        print("크롤링 끝!")
        break
    cnt += 1
    if cnt % 15 == 0:
        #스크롤을 내리면 20개의 추가 댓글이 보임을 확인함
        #로딩 시간이 길어지면 20개의 새로운 댓글 모두를 출력하지 못할 수도 있으므로 15개씩만 더 로딩되도 END키를 누르도록 설정
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(3)
        comments = browser.find_elements_by_css_selector("yt-formatted-string#content-text")

# for i in comments: #계속해서 스크롤도 내려줘야되니까 차라리 while문을 쓰는 게 낫다
#     print(i.text)