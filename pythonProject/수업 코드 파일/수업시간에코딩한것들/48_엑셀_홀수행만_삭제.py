import pandas as pd

df = pd.read_excel("./엑셀데이터/전자기기매출액.xlsx")
df[::2].to_excel("./엑셀데이터/전자기기매출액_짝수행만.xlsx", index=None)