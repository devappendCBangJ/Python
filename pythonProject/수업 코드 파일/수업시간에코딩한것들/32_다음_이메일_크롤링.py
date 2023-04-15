from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome("./chromedriver", options=option)
# 다음 로그인 사이트로 이동
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("button#loginBtn").click()
time.sleep(3)

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2)
# 이메일 제목 크롤링
# <beautifulsoup>
# 1. HTML코드 서버로부터 받아오기
# 2. HTML코드 이쁘게 정리하기
# 3. 원하는 요소 컴퓨터에게 알려주기.  --> select_one(), select()
# <selenium>
# 1. 원하는 요소 컴퓨터에게 알려주기.  --> find_element_by_css_selector(), find_elements_by_css_selector()
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)   # 뷰티풀숩은 ".string" / 셀레니움은 ".text"
browser.close()

# 셀레니움 장점
# 1. 크롤링을 못하는 곳이 없다.
# 2. 코드짜기 편하다.

# 셀레니움 단점
# 1. 느리다... 뷰티풀숩의 10배정도..
# 2. time.sleep()

# 셀레니움을 꼭 써야만 하는 상황
# 1. 로그인이 필요한 사이트
# 2. 웹페이지가 동적일 때

