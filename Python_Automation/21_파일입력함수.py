# <파일 입력 함수>
# 파일 열기(파일 없으면 오류) : open("경로/파일 이름.확장자", "파일 열기 모드", encoding='UTF8')
# - 경로 지정 안하면? : 파이썬 파일 저장 경로에 저장
# 파일 읽기 : open("경로/파일 이름.확장자", "파일 열기 모드", encoding='UTF8').read()
# 파일 닫기 : open("경로/파일 이름.확장자", "파일 열기 모드").close()

# <파일 열기 모드 종류>
# "r" 모드 : 읽기
# - 파일 그대로 읽기 : open("경로/파일 이름.확장자", "파일 열기 모드", encoding='UTF8').read()
# - 파일 한 줄 읽기 : open("경로/파일 이름.확장자", "파일 열기 모드", encoding='UTF8').readline()
# - 파일 그대로 읽기 & list형 반환 : open("경로/파일 이름.확장자", "파일 열기 모드", encoding='UTF8').readlines()

f = open("test.txt", "r", encoding='UTF8') #파일열기 모드
result = f.read() #파일에 있는 텍스트 그대로 불러옴
eeing = open("tedfafasdfst.txt", "r", encoding='UTF8')
f.close() #파일 닫기

print(result)