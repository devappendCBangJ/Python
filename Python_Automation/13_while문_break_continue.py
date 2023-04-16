# <while문> 반복문
# 조건 생성 : while 조건:
# 루프 시간 : 조건이 만족하는 한 무한 루프
# if문 이용 >> 루프 빠져나가기
#       1. while문의 처음으로 이동 : continue
#       2. 강제 탈출 : break

num = 0
while True: #무한루프 : True를 무조건 만족하므로 무한히 돌아감
    num += 1
    if num % 2 == 1: #num % 2 == 1 : num이 홀수라면?
        continue #반복문을 처음 조건부 문장으로 돌려보냄. 그러면 홀수 일때 print(num) 출력을 못하므로, 20까지의 짝수만 출력됨
    print("현재 num은 {}입니다.".format(num))
    if num == 20:  # a=b : 값 b를 a에 대입 / a==b : 조건부 문장에서 양쪽 값이 같은가?
        break  # 반복문 강제 탈출