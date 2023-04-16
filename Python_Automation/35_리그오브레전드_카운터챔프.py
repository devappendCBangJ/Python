#태그명:nth-child(?) : 같은 태그명인 자손이 있을 때, ?번째에 있는 자손을 불러옴

from selenium import webdriver
import time

your_champ = input("상대가 고른 챔프 입력 >> ")
browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://www.op.gg/champion/statistics")
time.sleep(3)

champs = browser.find_elements_by_css_selector("div.champion-index__champion-item__name")
for i in champs:
    if i.text == your_champ:
        i.click()
        break #for문을 빠져나감
time.sleep(3)

#<카운터 메뉴 클릭하기>
counter_menu = browser.find_element_by_css_selector("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader a")
#카운터 메뉴창을 누르면 html 코드가 active로 바뀌니까 누르지 않은 상태에서 검사를 실행해야함
counter_menu.click()
time.sleep(3)

#<카운터 챔프 크롤링>
counter = browser.find_elements_by_css_selector("div.champion-matchup-list__champion > span:nth-child(2)")
num = 1
for i in counter:
    print(num, " : ", i.text)
    num += 1
browser.close()