from selenium import webdriver
import time
import os
from twilio.rest import Client

browser = webdriver.Chrome("./chromedriver")
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 중고나라 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # 프레임전환
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(2)
# 과거의 게시글 제목이 들어가 있는 메모장 파일 불러옴.
try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except: # 파일이 존재하지 않으면, 파일 새로 생성
    f = open("./중고나라.txt", "w") # 파일이 존재하지 않으면, 파일을 새로 생성
    ref = []

# 게시물 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if not (i.text+"\n") in ref: # 크롤링한 제목이 최신의 글이라면?
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n")
        if "스마트폰" in i.text: # 관심있는 물건이라면?
            new_one += 1
f.close()
print("{} 관련 글이 {} 개 올라왔습니다.".format("스마트폰", new_one))
browser.close()

if new_one >= 1:
    account_sid = "ACfe94d937624be6d826061267764090f1"
    auth_token = "61aa55998b6f44049cc013c2461227b2"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="{} 관련 글이 {} 개 올라왔습니다.   http://cafe.daum.net/talingpython/rRa6".format("스마트폰", new_one),
                         from_='+19123333630',
                         to='+821095518905'
                     )




