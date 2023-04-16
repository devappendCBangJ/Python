# pip install mlxtend

# <텍스트마이닝 연관분석>
# 0. 데이터 프레임 함수 : import pandas as pd
# 0. 연관 분석 모듈 : from mlxtend.preprocessing import TransactionEncoder
# 0. 연관 분석 모듈 : from mlxtend.frequent_patterns import apriori
# 1. 데이터셋 지정 : dataset = [["","","",...], ["","","",...], ["","","",...], ["","","",...]...]
# 2. 전처리 : TransactionEncoder.fit(dataset).transform(dataset)
# 3. 데이터 프레임 형성 : df = pd.DataFrame(TransactionEncoder.fit(dataset).transform(dataset), columns=TransactionEncoder.columns_)
    # 데이터셋, 데이터 열 이름 자동 설정
# 4. 연관 확률 분석 : apriori(df, use_colnames=True) # support는 연관성을 나타냄
# 5. 연관 확률 출력 : print(apriori(df, use_colnames=True))

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# 데이터셋
dataset = [
    ["사과", "치즈", "생수"],
    ["생수", "치즈", "호두", "고등어"],
    ["사과", "옥수수", "복숭아"],
    ["생수", "치즈", "호두", "옥수수"],
]

# 전처리
te = TransactionEncoder()
te_transform = te.fit(dataset).transform(dataset)
print(te_transform) # 확인용 코드
df = pd.DataFrame(te_transform, columns=te.columns_)
print(df) # 확인용 코드

# 연관 확률 분석
df_apr = apriori(df, use_colnames=True) # support는 연관성을 나타냄
print(df_apr)