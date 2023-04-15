# google >> pyecharts example 검색 >> 공식 홈페이지 상단 En us 클릭 >> Charts base 클릭 >> Bar3D 클릭 >> 예제 코드 복붙 후 수정하여 사용
# 홈페이지에서 제공하는 예제에 맞는 버전인 pip install pyecharts==0.5.10
# pip install pyecharts_snapshot

# <텍스트마이닝 감성분석 & 차트 그리기>
# - 예제 수정해서 사용
# - 감성분석 학습 난이도 : 한국어 hard > 영어 easy

# {:.2f}.format(~~) 소수 2째자리까지 출력

# 텍스트마이닝 - 감성분석 함수(자료 제공 복붙)
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

okt = Okt()
tokenizer = Tokenizer(19417, oov_token = 'OOV')
with open('wordIndex.json') as json_file:
  word_index = json.load(json_file)
  tokenizer.word_index = word_index

loaded_model = load_model('best_model.h5')
def sentiment_predict(new_sentence):
    print(new_sentence)
    max_len = 30
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(pad_new)) # 예측
    if 0.8 <= score <= 1.0:
        return "매우긍정"
    elif 0.6 <= score < 0.8:
        return "긍정"
    elif 0.4 <= score < 0.6:
        return "보통"
    elif 0.2 <= score < 0.4:
        return "부정"
    else:
        return "매우부정"
    # return score

# 네이버 영화리뷰 크롤링(자료 제공 복붙)
from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
previous_page_result = ""
emotion_result = {"매우긍정":0, "긍정":0, "보통":0, "부정":0, "매우부정":0}
while True:
    code = req.urlopen("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=10106&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    comment = soup.select("li > div.score_reple > p > span")
    if comment[-1].text.strip() == previous_page_result:
        break
    for i in comment:
        i = i.text.strip()
        if i == "관람객":
            continue
        # print(i)
        result = sentiment_predict(i) # 감성 분석 결과 받음
        # if score >= 0.5:
        #     print("{:.2f}% 확률로 긍정입니다.".format(score*100)) # {:.2f} 소수 2째자리까지 출력
        # else:
        #     print("{:.2f}% 확률로 부정입니다.".format((1-score)*100))
        emotion_result[result] += 1
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    previous_page_result = i
    page_num += 1

# 감정분석 시각화
from pyecharts import Bar3D
from selenium import webdriver
import os

bar3d = Bar3D("감성 분석 결과", width=1200, height=600)
x_axis = ["매우 긍정", "긍정", "보통", "부정", "매우 부정"]
y_axis = []
data = [[0, 0, emotion_result["매우긍정"]], [0, 1, emotion_result["긍정"]], [0, 2, emotion_result["보통"]], [0, 3, emotion_result["부정"]], [0, 4, emotion_result["매우부정"]]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True, visual_range=[0, 180], visual_range_color=range_color,
    grid3d_width=200, grid3d_depth=40)
bar3d.render("./bar3d.html") # 파일 저장할 위치, 이름

abs_path = os.path.abspath("./bar3d.html")
browser1 = webdriver.Chrome("./chromedriver.exe")
browser1.get(abs_path)

# 감정분석 시각화
from pyecharts import Pie

attr = [emotion_result["매우긍정"], emotion_result["긍정"], emotion_result["보통"], emotion_result["부정"], emotion_result["매우부정"]]
v1 = [11, 12, 13, 10, 10]
pie = Pie("감성 분석 결과")
pie.add("", attr, v1, is_label_show=True)
pie.render("./pie.html") # 파일 저장할 위치, 이름

abs_path = os.path.abspath("./pie.html")
browser2 = webdriver.Chrome("./chromedriver.exe") # browser1 browser2로 구분하지 않으면, 가장 마지막 크롬 창이 처음 창을 덮어서 마지막 창만 보임
browser2.get(abs_path)