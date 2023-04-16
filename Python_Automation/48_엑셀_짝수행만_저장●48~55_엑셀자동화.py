# openpyxl 공부 사이트 : https://goodthings4me.tistory.com/487

# 모듈 쉽게 설치 : import 모듈 부분 클릭 후 Alt+Enter+Enter

#<자료 수집 모듈 pandas>
# - data frame은 대량의 데이터를 다룰 때 편리하고, 엑셀과의 궁합이 좋다
# 0. 판다스 모듈 불러오기 : import pandas as pd
    # 추가. 새로운 데이터 프레임 생성 : df_merge = pd.DataFrame()
# 1. 엑셀 파일 읽기 : df = pandas.read_excel("./파일 위치/파일명")
# 1. 엑셀 파일 특정 시트 읽기 : df = pandas.read_excel("./파일 위치/파일명", sheet_name="특정 시트 이름")
# 2. 엑셀 파일 필터링 : print(df[(df["지역명"] == "서울") & (df["분양가격"] >= 4000)]) #df[] 안에 조건 입력
# 2. 열에서 중복값 제외 고유한 값 리스트화 : df["열 제목"].unique()
# 3. 엑셀 파일 필터링 후 정렬 : print(df[df["지역명"] == "서울"].sort_values(by="분양가격", ascending=True))
    # - 정렬 기준 : by="열 제목"
    # - 오름차순 : ascending=True
    # - 내림차순 : ascending=False
# 4. 엑셀 파일 인덱스 변경 : df.set_index("불러올 열의 제목", inplace=True)
    # 추가. 새로운 데이터 프레임에 필요한 값 출력 : df_merge["새로운 열 제목"] = df["불러올 열의 제목"]
# 5. 엑셀 파일 범위 행 인덱스 포함 저장 : df[행1:행2:출력 행 배수].to_excel("./파일 위치/파일명")
# 5. 엑셀 파일 범위 행 인덱스 미포함 저장 : df[행1:행2:출력 행 배수].to_excel("./파일 위치/파일명", index=None)
# 5. 엑셀 파일 1개 특정 열 저장 : df["특정 열1"].to_excel(pd.ExcelWriter("./파일 위치/파일명"), sheet_name="새로운 시트 이름")
#                          pd.ExcelWriter("./파일 위치/파일명").save()
# 5. 엑셀 파일 2개 이상의 특정 열 저장 : df[["특정 열1", "특정 열2"...]].to_excel(pd.ExcelWriter("./파일 위치/파일명"), sheet_name="새로운 시트 이름")
#                          pd.ExcelWriter("./파일 위치/파일명").save()
    # 추가. 새로운 데이터 프레임 저장 : df_merge.to_excel("./파일 위치/파일명")

    # - 엑셀 파일 전체 행 출력 : print(df[:])
    # - 엑셀 파일 행1 ~ 행2 출력 : print(df[행1:행2])
    # - 엑셀 파일 전체 행 배수 출력 : print(df[::출력 행 배수])
    # - 엑셀 파일 행1 ~ 행2 배수 출력 : print(df[행1:행2:출력 행 배수])

import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel("./엑셀데이터/전자기기매출액.xlsx")

# 필요한 행만 뽑은 후 저장
df[::2].to_excel("./엑셀데이터/전자기기매출액_짝수행만.xlsx", index=None)
print(df[::2]) #확인용 코드