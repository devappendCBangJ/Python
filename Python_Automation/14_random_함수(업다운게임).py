# <랜덤 정수 함수>
# 랜덤 모듈 불러오기 : import random
# 0과 1사이의 랜덤한 소수 : random.random()
# 정수1과 정수2 사이의 랜덤한 정수 : random.randint(정수1, 정수2)



import random #random 함수를 import

ans = random.randint(1, 100) #1~100 사이의 랜덤한 숫자
print("---- 업 다운 게임을 시작합니다 ----")
count = 0
while True:
    num = int(input("숫자 입력 >> "))
    count += 1
    if num == ans:
        print("정답입니다!")
        break
    elif num > ans:
        print("DOWN!")
    elif num < ans:
        print("UP!")
print("{}회만에 정답을 맞히셨습니다.".format(count))