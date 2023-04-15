# <지역변수> 함수 안에서 만들어진 변수
# 접근 : 함수 안에서만 접근 가능

# <전역변수> 함수 밖에서 만들어진 변수
# 접근 : 모든 지역에서 접근 가능(read-only)
# 지역에서 전역변수 수정 : 지역에서 global 전역변수 선언 >> 값 수정

def func1():
    a = 1 #지역변수
func1()
# print(a) #확인용 코드


num = 10 #전역변수

def func2():
    global num #전역변수 num 값 수정 허락맡기
    num += 1
    print(num)
func2()