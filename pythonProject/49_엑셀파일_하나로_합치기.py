# 리스트 생성후 그것을 이용한 for문

import pandas as pd

# 새로운 데이터 프레임 형성
df_merge = pd.DataFrame()

# 엑셀 파일 읽음 + 인덱스 변경 + 필요한 열만 뽑은 후 저장
company = ["LG전자", "삼성전자", "현대자동차"]
for i in company:
    df = pd.read_excel("./엑셀데이터/2017년_광고비_{}.xlsx".format(i))
    df.set_index("date", inplace=True)
    df_merge[i] = df["total"]
df_merge.to_excel("./엑셀데이터/2017년_광고비_total.xlsx")