from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.youtube.com/watch?v=eYWF8fupl88")
time.sleep(4)

# 맨 처음에 스크롤 조금 내려주기.
# browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
# 맨 처음에 스크롤 끝까지 내려주기.
# browser.find_element_by_css_selector("html").send_keys(Keys.END)
# time.sleep(3)

# 댓글 크롤링
comments = browser.find_elements_by_css_selector("#content-text")
cnt = 0
while True:
    try:
        print(comments[cnt].text)
    except:
        print("크롤링 끝!")
        break
    cnt += 1
    # 댓글을 15개, 30개, 45개, 60개 출력할때마다....
    # 스크롤 끝까지 내려주기..
    if cnt % 15 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(3)
        comments = browser.find_elements_by_css_selector("#content-text")






