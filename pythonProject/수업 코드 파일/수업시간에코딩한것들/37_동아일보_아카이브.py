import requests
from bs4 import BeautifulSoup

sess = requests.session() # 세션 만들기
data = {
"idsave_value": "",
"errorChk": "",
"gourl": "https://www.donga.com/archive/newslibrary/view?ymd=19991129&mode=19991129/0002371757/1",
"bid": "talingpython",
"bpw": "xkfdldvkdlTjs2"
}
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19991129%26mode%3D19991129%2F0002371757%2F1"}
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=h, data=data) # post 요청

code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19991129&mode=19991129/0002371757/1")
soup = BeautifulSoup(code.text, "html.parser")
title = soup.select("ul.news_list a")
for i in title:
    print(i.string)
    content_num = i.attrs["onclick"].replace("javascript:getNewsArticle('19991129/", "").replace("/1'); return false;", "")
    content_url = "https://www.donga.com/archive/newslibrary/view?idx=19991129%2F{}%2F1".format(content_num)
    code = sess.get(content_url)
    soup = BeautifulSoup(code.text, "html.parser")
    content = soup.select_one("div.article_txt")
    print(content.text.strip())
    print()














