import pandas as pd

writer = pd.ExcelWriter("./엑셀데이터/장사시설현황_합치기.xlsx")
for year in range(2017, 2021):
    df = pd.read_excel("./엑셀데이터/장사시설현황_2017년_2020년/{}년 장사시설 현황/전국장사시설현황.xlsx".format(year), sheet_name="장례식장 시설정보")
    df[["시설명", "주소"]].to_excel(writer, sheet_name="{}년".format(year))
writer.save()
