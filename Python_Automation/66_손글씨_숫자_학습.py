import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# 데이터 불러오기
train = pd.read_csv("./mnist/train.csv")
valid = pd.read_csv("./mnist/t10k.csv")

# 데이터 쪼개기
train_label = train.iloc[:, 0]
train_data = train.iloc[:, 1:]

valid_label = valid.iloc[:, 0]
valid_data = valid.iloc[:, 1:]

# 학습 알고리즘 선택
model = SVC()

# 학습
model.fit(train_data, train_label)

# 정답 예측
result = model.predict(valid_data)

# 예측값과 정답 비교 채점
score = accuracy_score(result, valid_label)
print(score)

# 모델 저장할 위치, 형식
f = open("./mnist_model.pkl", "wb")

# 모델 저장
pickle.dump(model, f)
f.close