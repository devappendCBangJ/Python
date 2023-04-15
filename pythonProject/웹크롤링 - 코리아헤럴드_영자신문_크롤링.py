# result = re.sub(r'(\\[x]..)|(\\r)|(\\n)|(\\t)|(\(Yonhap\))', "", contents.text.strip())  이건뭐지????????????????????

import urllib.request as req
from bs4 import BeautifulSoup
import re

keyword = input("영어로 키워드 입력 >> ")
page_num = 1
while True:
    # 기사 가져오기
    url = "http://www.koreaherald.com/search/index.php?q={}&sort=1&mode=list&np={}&mp=1".format(keyword, page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    articles = soup.select("ul.main_sec_li > li > a")
    if len(articles) == 0:
        break
    # 기사 제목, 내용 가져오기
    for i in articles:
        title = i.select_one("div.main_l_t1")
        print("제목 :", title.text)
        link = "http://www.koreaherald.com" + i.attrs["href"]
        code_news = req.urlopen(link)
        soup_news = BeautifulSoup(code_news, "html.parser")
        contents = soup_news.select_one("div#articleText")
        # 데이터 가공
        result = re.sub(r'(\\[x]..)|(\\r)|(\\n)|(\\t)|(\(Yonhap\))', "", contents.text.strip())
        print(result)
        print()
    page_num += 1