import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
from konlpy.tag import Okt
from collections import Counter
import wordcloud
import matplotlib.pyplot as plt  # pip install matplotlib
from PIL import Image  # pip install pillow
import numpy as np # pip install numpy

keyword = "코딩"
encoded = par.quote(keyword)
page_num = 1
output_total = ""
while True:
    url = "https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: # 끝 페이지까지 크롤링을 완료했다면?
        break
    for i in title:
        print("제목 :", i.text)
        print("링크 :", i.attrs["href"])
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("  ", "")
        print(result)
        print()
        output_total += result
    page_num += 1
    if page_num == 2:
        break

# 형태소 분석
okt = Okt()
nouns_list = okt.nouns(output_total)
# print(nouns_list)
# 불용어 제거
for noun in nouns_list:
    if len(noun) == 1:
        nouns_list.remove(noun)
# print(nouns_list)
cnt = Counter(nouns_list)
print(cnt)

# 이미지 불러오기.
image_list = np.array(Image.open("./image.png"))
image_color = wordcloud.ImageColorGenerator(image_list)

# 단어구름 만들기
cloud_image = wordcloud.WordCloud(font_path="./NanumMyeongjoBold.ttf", background_color="white", mask=image_list).generate_from_frequencies(cnt)
# 단어구름 이미지 띄우기
plt.figure(figsize=(10,10))
plt.imshow(cloud_image.recolor(color_func=image_color), interpolation="bilinear")
plt.axis("off")
plt.show()








