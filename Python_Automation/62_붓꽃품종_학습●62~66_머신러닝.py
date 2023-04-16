# <모듈, 패키지 개념>
    # 관계 : 변수 < 함수 < 클래스 < 모듈 < 패키지
        # - 모듈 : 특정 기능을 .py 파일 단위로 작성
        # - 패키지 : 여러 모듈의 묶음
        # - 라이브러리 : 여러 패키지의 묶음
    # 사용 방법 :
        # 모듈 가져오기
            # - import 패키지.모듈
            # - import 패키지.모듈1, 패키지.모듈2
            # - import 패키지.모듈.변수
            # - import 패키지.모듈.함수()
            # - import 패키지.모듈.클래스()
        # 모듈 해제
            # - del 패키지.모듈
        # 모듈 다시 가져오기
            # - import math
            # - importlib.reload(math)
        # if __name__=='__main__': 현재 스크립트 파일이 프로그램의 시작점인지 모듈인지 판단(스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분)

# <인공지능, 머신러닝, 딥러닝>
    # 인공지능 > 머신러닝 > 딥러닝
        # 1. 인공지능
            # 1) 알고리즘 종류
                # - SVC(Support Vector Machine) : 직선 사용 분리
                # - KNN(최근접 이웃 알고리즘) : 타겟 근처 좌표 값 활용
                # - Decision Tree(의사결정 트리) : 다양한 질문을 통한 분류
                # - Random Forest()
            # 2) 다양한 알고리즘
                # from sklearn.neural_network import	MLPClassifier
                # from sklearn.neighbors import	MLPClassifier
                # from sklearn.svm SVC	import	SVC
                # from sklearn.gaussian_process import	GaussianProcessClassifier
                # from sklearn.gaussian_process.kernels import RBF
                # from sklearn.tree import DecisionTreeClassifier
                # from sklearn.ensemble import RandomForestClassifier,	AdaBoostClassifier
                # from sklearn.naive_bayes import GaussianNB
                # from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
        # 2. 머신러닝
            # 1) 지도학습 : 강의 >> 정답 찾기 or 연관성 증명
                # (1) 지도학습 순서 : 특징 추출 >> 좌표 표시 >> 규칙 형성 >> 예측 >> 피드백
                # - labal : 정답
                    # 분류 모델 : label이 딱 떨어지는 값
                    # 회귀 모델 : label이 연속적인 값
                # - data : 나머지 특징들
            # 2) 비지도학습 : 자습 >> 분류
            # 3) 강화학습 : 보상 강의 >> 정답 찾기
        # 3. 딥러닝(Deep Neural Network)

# <머신러닝 분류 알고리즘 순서>
    # 0. 데이터 분석 모듈 : import pandas
    # 0. 머신러닝 분류 알고리즘 모듈 : from sklearn.svm import SVC
    # 0. 머신러닝 학습, 테스트 데이터셋 랜덤 분리 모듈 : from sklearn.model_selection import train_test_split
    # 0. 머신러닝 비교 채점 모듈 : from sklearn.metrics import accuracy_score
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
    # 4. 학습 알고리즘 선택 : model = SVC()
    # 5. 학습 : model.fit(train_data, train_label)
    # 6. 정답 예측 : result = model.predict(valid_data)
    # 7. 예측값과 정답 비교 채점 : score = accuracy_score(result, valid_label)
    # 8. 모델 저장 위치, 형식 설정 및 저장 :
        # f = open("파일 위치/파일명.pkl", "wb")
        # pickle.dump(model, f)
        # f.close

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 불러오기
df = pd.read_csv("./머신러닝/iris.csv")
label = df["variety"]
data = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]

# 데이터 쪼개기
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

# 학습 알고리즘 선택
model = SVC() #Support Vector Machine Classifier

# 학습
model.fit(train_data, train_label)

# 정답 예측
# result = model.predict([[4.2, 1.2, 5.4, 2.3], [1.2, 4.2, 6.8, 6.7], [2.1, 1.02, 1.8, 4.2]])
result = model.predict(valid_data)
print("result : ", result)

# 예측값과 정답 비교 채점
score = accuracy_score(result, valid_label)
print(score)
