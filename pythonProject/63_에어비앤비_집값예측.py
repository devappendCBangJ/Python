# <머신러닝 회귀 알고리즘 순서>
# 0. 데이터 분석 모듈 : import pandas
# 0. 머신러닝 회귀 알고리즘 모듈 : sklearn.linear_model import LinearRegression
# 0. 머신러닝 학습, 테스트 데이터셋 랜덤 분리 모듈 : from sklearn.model_selection import train_test_split
# 0. 머신러닝 회귀 알고리즘 채점 모듈 : from sklearn.metrics import mean_squared_error
# 1. 데이터 전처리 :
    # - 문자열 >> 숫자 변환
    # - 데이터 구간화
# 2. 데이터 불러오기 :
    # df = pd.read_csv("./파일 위치/파일명")
    # label = df["타겟 열 제목"]
    # 열 기준 불러오기 : data = df[["열1 제목", "열2 제목", "열3 제목", "열4 제목", ...]]
    # 행, 열 편리하게 불러오기 : data = df.iloc[행1:행2, 열1:열2]
# 3. 데이터 쪼개기 :
    # train_data, valid_data, train_label, valid_label = train_test_split(data, label)
# 4. 학습 알고리즘 선택 : model = LinearRegression()
# 5. 학습 : model.fit(train_data, train_label)
# 6. 정답 예측 : result = model.predict(valid_data)
# 7. 예측값과 정답 비교 채점 : score = mean_squared_error(result, valid_label) ** (1/2)
# 8. 모델 저장 위치, 형식 설정 및 저장 :
    # f = open("파일 위치/파일명.pkl", "wb")
    # pickle.dump(model, f)
    # f.close

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 데이터 불러오기
df = pd.read_csv("./머신러닝/Airbnb.csv")
label = df["price"]
data = df.iloc[:, 0:6]

# 데이터 쪼개기
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

# 학습 알고리즘 선택
model = LinearRegression()

# 학습
model.fit(train_data, train_label)

# 정답 예측
result = model.predict(valid_data)
print(result)
my_house_result = model.predict([[0.000321, 0.43, 6.3, 4.1, 30, 50]])
print(my_house_result)

# 예측값과 정답 비교 채점
score = mean_squared_error(result, valid_label) ** (1/2)
print(score)