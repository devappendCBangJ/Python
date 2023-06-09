# <텍스트마이닝 감성분석>
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
    return score

# 네이버 영화리뷰 크롤링(자료 제공 복붙)
from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
previous_page_result = ""
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
        score = sentiment_predict(i)
        if score >= 0.5:
            print("{:.2f}% 확률로 긍정입니다.".format(score*100))
        else:
            print("{:.2f}% 확률로 부정입니다.".format((1-score)*100))
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    previous_page_result = i
    page_num += 1