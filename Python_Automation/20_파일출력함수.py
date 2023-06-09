# <파일 출력 함수>
# 파일 열기(없으면 생성 후 열기) : open("경로/파일 이름.확장자", "파일 열기 모드")
# - 경로 지정 안하면? : 파이썬 파일 저장 경로에 저장
# 파일 쓰기 : open("경로/파일 이름.확장자", "파일 열기 모드").write(내용)
# 파일 닫기 : open("경로/파일 이름.확장자", "파일 열기 모드").close()

# <파일 열기 모드 종류>
# "w" 모드 : 초기화 후 쓰기
# - 파일의 내용을 모두 지운 후, 다시 파일을 연다
# "a" 모드 : 더해서 쓰기
# - 파일의 내용을 모두 유지한 후, 다시 파일을 연다

#\n : 한 줄 띄워서 출력

f = open("C:/Users/Bang/Desktop/test.ppt", "w") #파일열기 모드

f.write("Hello\n") #\n : 한 줄 띄워서 출력
f.write("World\n")
f.write("Python\n")
f.close() #파일 닫기