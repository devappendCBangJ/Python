import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def normalize_list(original_list):
    total_cnt = sum(original_list)
    normalized_list = []
    for i in original_list:
        normalized_list.append(i/total_cnt)
    return normalized_list

def frequency_alphabet(text):
    text = text.lower()  # 소문자 변환

    # 알파벳 출현 빈도 구하기
    code_a = ord("a")
    code_z = ord("z")
    cnt = [0 for n in range(0, 26)]  # 26개의 0
    for char in text:
        code_current = ord(char)
        if code_a <= code_current <= code_z:
            cnt[code_current - code_a] += 1
    return normalize_list(cnt)

def get_data_label(folder_name):
    files = glob.glob("./머신러닝/language/{}/*.txt".format(folder_name))  # 폴더 내 텍스트 파일 추출
    data = []
    label = []

    for fname in files:
        # 레이블 구하기
        basename = os.path.basename(fname)
        lang = basename.split("-")[0]

        # 텍스트 추출하기
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()
        cnt = frequency_alphabet(text)

        # 리스트에 넣기
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


train_data, train_label = get_data_label("train")
valid_data, valid_label = get_data_label("test")
# show_me_the_graph(train_data, train_label)
# 학습시키기
model = SVC()
model.fit(train_data, train_label)
# 정확도 확인하기
result = model.predict(valid_data)
score = accuracy_score(result, valid_label)
print(score)

test_string = """Ang Python Programming Language ay binuo ni "Guido Van Rossum" nung huling bahagi ng dekada 80 nung siya ay isang mananaliksik pa lamang sa Centrum Wiskunde & Informatica (CWI) o Center for Mathematics and Computer Science sa Amsterdam, Netherlands. Sa katanuyan nabuo ito bilang isang proyekto para may mapagkaabalahan lamang si Guido sa kanyang Christmas vacation noong Disyembre 1989. Di naglaon naging bahagi ito ng proyektong Amoeba sa CWI at ini-release sa publiko ito noong Pebrero 1991.

Hindi galing sa sawa ng pamilyang Pythonidae ang pangalan ng computer language na ito kundi galing sa isang grupo ng komedyanteng taga-Britanya na kung tawagin ay "Monty Python's Flying Circus".

Ang Python ay isang makabagong uri ng mataas na antas na programming language na kung saan ginagamit na dito ang mga elemento at termino na gaya ng isang natural na wika, kung kaya't madali itong gamitin at maaring ilipat sa kahit na anong platform. Halimbawa, pwedeng isulat ang python code sa Mac OS, i-test ito sa anumang uri ng Linux at i-upload sa Windows NT na hindi na kailangang baguhin pa ang mga code."""

test_string_cnt = frequency_alphabet(test_string)
result = model.predict([
    test_string_cnt
])
print(result)


