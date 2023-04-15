import pandas as pd

# 엑셀 불러오기
df = pd.read_excel("./엑셀데이터/아파트분양가격.xlsx")

# 조건에 맞는 값 출력
df_seoul = df[df["지역명"] == "서울"]
result = df_seoul.sort_values(by="분양가격", ascending=True)
print(result)