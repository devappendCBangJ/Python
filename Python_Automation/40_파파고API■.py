# 파파고 API 무료 ver : 하루 10000자 제한
# 파파고 API 유료 ver : 하루 더 많은 양 번역 가능

# <re ????????????????????>
# result = re.sub(r'(\\[x]..)|(\\r)|(\\n)|(\\t)|(\(Yonhap\))', "", contents.text.strip())

import urllib.request as req
from bs4 import BeautifulSoup
import re

import os
import sys
import urllib.request
import json

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
        # print(result) #영어 기사 출력
        # print()

        # 파파고 api 번역
        if len(result) > 5000:
            result = result[0:5000]

        api_id = "★api_id★"
        api_pw = "★api_pw★"

        client_id = api_id  # 개발자센터에서 발급받은 Client ID 값
        client_secret = api_pw  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(result)
        data = "source=en&target=ko&text=" + encText #source언어와 target언어 설정
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            result_dict = json.loads(result)  # json -> 딕셔너리
            print(result_dict["message"]["result"]["translatedText"])
            print()
        else:
            print("Error Code:" + rescode)

    page_num += 1