from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("./머신러닝/Airbnb.csv")
label = df["price"]
data = df.iloc[:, 0:6]
train_data, valid_data, train_label, valid_label = train_test_split(data, label)
# 학습시키기
model = LinearRegression()
model.fit(train_data, train_label)
# 정확도 확인하기
result = model.predict(valid_data)
score = mean_squared_error(result, valid_label) ** (1/2)
print(score)

my_house = model.predict([
    [0.000321, 0.43, 6.3, 4.1, 30, 50]
])

print(my_house)