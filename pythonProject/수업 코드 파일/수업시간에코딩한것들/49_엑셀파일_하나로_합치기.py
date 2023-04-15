import pandas as pd

df_merge = pd.DataFrame()

company = ["LG전자", "삼성전자", "현대자동차"]
for i in company:
    df = pd.read_excel("./엑셀데이터/2017년_광고비_{}.xlsx".format(i))
    df.set_index("date", inplace=True)
    df_merge[i] = df["total"]
df_merge.to_excel("./엑셀데이터/2017년_광고비_total.xlsx")


