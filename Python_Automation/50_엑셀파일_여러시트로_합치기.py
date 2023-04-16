import pandas as pd

#엑셀 파일 읽기
writer = pd.ExcelWriter("./엑셀데이터/장사시설현황_합치기.xlsx") #pandas에 엑셀 기능 확장

# 필요한 열만 뽑은 후 저장
for year in range(2017, 2021):
    df = pd.read_excel("./엑셀데이터/장사시설현황_2017년_2020년/{}년장사시설현황/전국장사시설현황.xlsx".format(year), sheet_name="장례식장 시설정보")
    # print(df[["시설명", "주소"]]) #확인용 코드
    df[["시설명", "주소"]].to_excel(writer, sheet_name="{}년".format(year))
writer.save()