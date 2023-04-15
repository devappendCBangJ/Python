# <아스키 코드값 반환 함수>
# 아스키 코드값 반환 : ord("문자")

import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 정규화 : 숫자의 범위 0~1 사이로 줄임... 컴퓨터는 높은 숫자 = 높은 중요도라고 판단하기 때문에, 숫자의 범위를 줄여줘서 각각의 중요도를 동일하게 판단하도록 설정
def normalize_list(original_list):
    total_cnt = sum(original_list)
    normalized_list = []
    for i in original_list:
        normalized_list.append(i/total_cnt)
    return normalized_list

# 알파벳 빈도 추출
def frequency_alphabet(text):
    # 소문자 변환
    text = text.lower()

    # 알파벳 아스키 코드 추출
    code_a = ord("a")
    code_z = ord("z")
    
    # 알파벳 아스키 코드 출현 빈도 추출
    cnt = [0 for n in range(0, 26)]  # 26개의 0
    for char in text:
        code_current = ord(char)
        if code_a <= code_current <= code_z:
            cnt[code_current - code_a] += 1
    return normalize_list(cnt)

# 데이터셋 추출
def get_data_label(folder_name):
    # 폴더 내 텍스트 파일 추출
    files = glob.glob("./머신러닝/language/{}/*.txt".format(folder_name))
    data = []
    label = []

    for fname in files:
        # 파일명 추출
        basename = os.path.basename(fname)
        lang = basename.split("-")[0]

        # 파일 읽기 모드, 텍스트 추출
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()
        cnt = frequency_alphabet(text)

        # lang, 알파벳별 cnt 리스트에 넣기
        label.append(lang)
        data.append(cnt)
    return data, label


def show_me_the_graph(data, label):
    # 그래프 준비하기
    graph_dict = {}
    for i in range(0, len(data)):
        y = label[i]
        x = normalize_list(data[i])
        if not (y in graph_dict):
            graph_dict[y] = x

    asclist = [[chr(n) for n in range(97, 97 + 26)]]
    df = pd.DataFrame(graph_dict, index=asclist)
    # 바그래프
    df.plot(kind='bar', subplots=True, ylim=(0, 0.15))
    plt.show()

# 데이터 불러오기, 쪼개기
train_data, train_label = get_data_label("train")
valid_data, valid_label = get_data_label("test")
# show_me_the_graph(train_data, train_label)

# 학습 알고리즘 선택
model = SVC()

# 학습
model.fit(train_data, train_label)

# 정답 예측
result = model.predict(valid_data)

# 예측값과 정답 비교 채점
score = accuracy_score(result, valid_label)
print(score)


# 데이터셋 추출
test_string = """La page de discussion de l'article « Python » n'existe pas encore.
Si votre question ne concerne pas directement la rédaction de l'article « Python », visitez plutôt Aide:Poser une question.

Sinon, laissez votre message dans la boîte ci-dessous.

N'oubliez pas de signer vos messages (aide) en tapant quatre tildes (~~~~) ou en cliquant sur le bouton"""

# 알파벳 빈도 추출
test_string_cnt = frequency_alphabet(test_string)

# 정답 예측
result = model.predict([test_string_cnt])
print(result)