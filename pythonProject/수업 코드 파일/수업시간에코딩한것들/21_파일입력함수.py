# 파일 열기 모드
# "r" 모드 : 읽기모드
# 파일이 존재하지 않으면, 에러!
f = open("qweqjrqwjfoiajs.txt", "r")
result = f.readlines()
f.close()

print(result)