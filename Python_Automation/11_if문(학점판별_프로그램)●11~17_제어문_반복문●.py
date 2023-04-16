# <if문> 조건문
# 조건 생성 : if 조건:
# if를 만족하지 않는 또다른 조건 : elif 조건:
# if와 elif 모두 만족하지 않는 모든 조건 : else 조건:
# 조건 판별 : == 기호 이용

score = int(input("점수 입력 >> "))
if score >= 90: #if문 선언
    print("학점 : A")
elif 80 <= score < 90: #elif : if의 경우가 아닌 또 다른 경우라면
    print("학점 : B")
elif 70 <= score < 90: #elif : if의 경우가 아닌 또 다른 경우라면
    print("학점 : C")
else: #else : 위의 모든 경우가 아닌 나머지 경우라면
    print("학점 : F")