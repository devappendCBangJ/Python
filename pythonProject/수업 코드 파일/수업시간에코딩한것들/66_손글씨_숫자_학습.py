from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

train = pd.read_csv("./mnist/train.csv")
valid = pd.read_csv("./mnist/t10k.csv")

train_label = train.iloc[:, 0]
train_data = train.iloc[:, 1:]

valid_label = valid.iloc[:, 0]
valid_data = valid.iloc[:, 1:]

model = SVC()
model.fit(train_data, train_label)

result = model.predict(valid_data)
score = accuracy_score(result, valid_label)
print(score)

f = open("./mnist_model.pkl", "wb")
pickle.dump(model, f)
f.close()

