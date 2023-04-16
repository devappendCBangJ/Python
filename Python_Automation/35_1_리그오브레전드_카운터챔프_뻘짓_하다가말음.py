from selenium import webdriver
import time
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def input_id_pw(browser, css, user_input):
    pyperclip.copy(user_input)  # input을 클립보드로 복사
    browser.find_element_by_css_selector(css).click()  # element focus 설정
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # 윈도우 : Ctrl+V 전달
    # ActionChains(browser).key_down(Keys.LEFT_SHIFT).key_down(Keys.INSERT).key_up(Keys.LEFT_SHIFT).key_up(Keys.INSERT).perform()  # 맥 : shift+insert 전달
    browser.find_element_by_css_selector("div.FPdoLc.lJ9FBc input.gNO89b").click()
    time.sleep(1)

option = webdriver.ChromeOptions()
# option.add_argument("headless") #크롬 브라우저 실행 시 옵션 설정
browser = webdriver.Chrome("./chromedriver.exe", options=option)
browser.get("https://www.google.com/")

user_input1 = input("검색어를 입력하세요 >> ")
input_id_pw(browser, "input.gLFyf.gsfi", user_input1)
time.sleep(1)