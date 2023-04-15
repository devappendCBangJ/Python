from selenium import webdriver
import time

your_champ = input("상대가 고른 챔프 입력 >> ")
browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.op.gg/champion/statistics")
time.sleep(3)

champs = browser.find_elements_by_css_selector("div.champion-index__champion-item__name")
for i in champs:
    if i.text == your_champ:
        i.click()
        break
time.sleep(3)

# 카운터 메뉴 클릭하기
browser.find_element_by_css_selector("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a").click()
time.sleep(2)

# 카운터 챔프 크롤링
counter = browser.find_elements_by_css_selector("div.champion-matchup-list__champion > span:nth-child(2)")
for i in counter:
    print(i.text)
browser.close()





