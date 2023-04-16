for eeing in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: #비효율적
    print("Hello World")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for eeing in range(1): #range(00) : 0~지정 정수 직전까지 정수 횟수 반복
    #range()의 숫자값들이 리스트 원소 하나하나 처럼 사용됨
    print("Hello World")
    print(eeing)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for eeing in range(10, 51): #range(00, 99) : 00~99 바로 직전 정수까지 정수 횟수 반복
    print("Hello World")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for eeing in range(0, 101, 3): #range(00, 99, 5) : 00~99 바로 직전 정수까지 정수 횟수 반복. 단, 5의 배수는 제외
    print(eeing)