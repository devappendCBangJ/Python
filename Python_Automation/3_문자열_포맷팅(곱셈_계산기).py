# <문자열 포맷팅>
# "~~{}~~".format() : 문자열 포맷팅
    # \ : 문자 입력 중 특정 명령 지시
    # ex. print("I really \"need\" this) >> I really "need" this

num1 = int(input("첫번째 숫자 입력 >> "))
num2 = int(input("두번째 숫자 입력 >> "))
print("곱셈 결과는 {}입니다.".format(num1 * num2))