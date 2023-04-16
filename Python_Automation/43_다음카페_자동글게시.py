#웹페이지의 시작 : Elements 소스코드에서 html 태그명으로 시작

#Selenium 개발 시 자주 표시되는 오류 : [No Such Element..Error]
#1. css 선택자 오타
#2. time.sleep() 길이
#3. html이 전체 코드 중간에 뜨는가? >> !프레임! 안에 들어있는지?

#프레임 전환은 바깥에서 안쪽 방향으로만 가능
#프레임 전환을 안쪽에서 바깥으로 하려면 디폴트로 돌려주고 다시 바깥에서 안쪽 방향으로 실행해야함

# 프레임 안쪽으로 전환 : webdriver.Chrome("크롬 드라이버 위치/크롬 드라이버 파일명").switch_to.frame(webdriver.Chrome("크롬 드라이버 위치/크롬 드라이버 파일명").find_element_by_css_selector("프레임 요소"))
# 프레임 디폴트 값으로 전환 : webdriver.Chrome("크롬 드라이버 위치/크롬 드라이버 파일명").switch_to.default_content()

from selenium import webdriver
import time

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

# 가입인사 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down"))
browser.find_element_by_css_selector("#fldlink_lF1R_309").click()
time.sleep(3)

# 글쓰기 버튼 클릭
browser.find_element_by_css_selector("#article-write-btn").click()
time.sleep(3)

# 제목 작성
subject = browser.find_element_by_css_selector(".title__input")
subject.send_keys("안녕하세요!")

# 본문 작성
browser.switch_to.frame(browser.find_element_by_css_selector("#keditorContainer_ifr")) # 프레임 전환
content = browser.find_element_by_css_selector("#tinymce")
content.send_keys("반갑습니다.")

# 발행 버튼 클릭
browser.switch_to.default_content()
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # 프레임 전환
browser.find_element_by_css_selector("button.btn_g.full_type1").click()
time.sleep(3)

# 브라우저 닫기
browser.close()