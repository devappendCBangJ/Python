# pip install wordcloud
# pip install matplotlib
# pip install pillow
# pip install numpy

# <텍스트마이닝 순서>
# 0. 형태소 분석 모듈 불러오기 : import konlpy
# 0. 형태소 분석 모듈 불러오기 : from konlpy.tag import Okt
# 0. 단어 빈도수 표현 모듈 불러오기 : from collections import Counter
# 0. 선형대수 모듈 불러오기 : import numpy as np
# 0. 이미지 모듈 불러오기 : from PIL import Image
# 0. 단어 구름 모듈 불러오기 : import wordcloud
# 0. 그래프 시각화 모듈 불러오기 : import matplotlib.pyplot as plt
# 1. 형태소 분석 후 리스트형 안에 튜플형으로 저장 : Okt.pos("형태소 분석할 글")
# 1. 형태소 분석 후 명사만 추출하여 리스트형 안에 튜플형으로 저장 : Okt.nouns("형태소 분석할 글")
# 2. 단어 빈도수 딕셔너리형으로 저장 : Counter(Okt.nouns("형태소 분석할 글"))
# 2-1. 불용어 제거
    # nouns_list = okt.nouns("형태소 분석할 글")
    # for noun in nouns_list:
    #     if len(noun) == 1:
    #         nouns_list.remove(noun)
# 3. 이미지 픽셀값을 리스트에 숫자 형태로 넣기 : image_list = np.array(Image.open("파일 위치/파일 이름"))
    # - 색이 너무 다양하면 단어 구름 색 추출에서 오류 발생
# 4. 이미지 픽셀값 색 추출 by 단어 구름 모듈 : image_color = wordcloud.ImageColorGenerator(image_list)
# 5. 단어 구름 이미지 저장 by 단어 구름 모듈 : cloud_image = wordcloud.WordCloud(font_path = "./NanumMyeongjoBold.ttf", background_color = "white", mask = image_list).generate_from_frequencies(Counter(Okt.nouns("형태소 분석할 글")))
    # - matplotlib은 근본적으로 한글 폰트 지원 x. 폰트 다운 후 지정해주기
# 6. 단어 구름 이미지 띄우기 by 그래프 시각화 모듈
    # 그래프 시각화 사이즈 설정 : plt.figure(figsize=(가로 인치, 세로 인치))
    # 그래프 시각화 축 없애기 : plt.axis("off")
    # 그래프 시각화 이미지 설정 & 이중선형 필터링 : plt.imshow(cloud_image.recolor(color_func=image_color), interpolation="bilinear")
    # 그래프 시각화 : plt.show()


import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
from konlpy.tag import Okt
from collections import Counter
import wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 31. 중앙일보_뉴스크롤링
keyword = "코딩"
encoded = par.quote(keyword)
page_num = 1

output_total = ""

while True:
    code = req.urlopen("https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded))
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: #끝 페이지까지 크롤링을 완료해서 title의 원소개수가 0개가 된다면
        break
    for i in title:
        print("제목 :", i.text)
        # 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용
        #i.text와 title[i].text는 같음
        print("링크 :", i.attrs["href"])
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("   ", "")
        print(result)
        # 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용
        print() #개행
        output_total += result # 형태소 분석을 위해 본문 전부를 끊김없이 이어지게 만들어줌
    page_num += 1 #페이지가 넘어가면 url주소가 아예 바뀌니까
    # while안에 정의한 url 주소와 같은 곳에 두기 위해 for문 밖으로 빼둠
    if page_num == 2:
        break
    
# 형태소 분석
okt = Okt()
nouns_list = okt.nouns(output_total)
print(nouns_list) # 확인용 코드

# 불용어 제거
for noun in nouns_list:
    if len(noun) == 1:
        nouns_list.remove(noun)
# print(nouns_list) # 확인용 코드
cnt = Counter(nouns_list)
print(cnt)

# 이미지 불러오기
image_list = np.array(Image.open("./image.jpg"))

# 단어 구름 이미지 만들기
image_color = wordcloud.ImageColorGenerator(image_list)
cloud_image = wordcloud.WordCloud(font_path="./NanumMyeongjoBold.ttf", background_color = "white", mask=image_list).generate_from_frequencies(cnt) # matplotlib은 한글 폰트 지원을 안해서 다운 받아서 넣어줘야함

# 단어 구름 이미지 띄우기
plt.figure(figsize=(10,10))
plt.axis("off")
plt.imshow(cloud_image.recolor(color_func=image_color), interpolation="bilinear")
plt.show()