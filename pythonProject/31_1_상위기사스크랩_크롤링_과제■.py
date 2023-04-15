import urllib.request as req
from bs4 import BeautifulSoup

headers = req.Request("https://news.naver.com/main/home.nhn", headers = {"User-Agent":"Mozilla/5.0"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
topic = soup.select("h4.tit_sec > a")
# print(topic.string) #topic은 리스트형이므로 []없이 사용 못함
# print(topic[0].string)
# print(len(topic)) #len(topic) : 리스트형에 len을 씌우면 리스트 개수를 출력함
topic_num = 0

for i in range(len(topic)):
    print("토픽 : ", topic[i].string)
    # news_code = req.urlopen("https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1={}".format(100+change_topic))
    # news_soup = BeautifulSoup(news_code, "html.parser")
    # title = soup.select_one("div.cluster_text > a")
    headers2 = req.Request("https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1={}".format(100 + i), headers={"User-Agent":"Mozilla/5.0"})
    news_code = req.urlopen(headers2)
    news_soup = BeautifulSoup(news_code, "html.parser")
    title = news_soup.select("div.cluster_text > a")
    for ii in range(3):
        print("   타이틀 : ", title[ii].string)