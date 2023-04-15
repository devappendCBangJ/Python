def func1():
    a = 1  # 지역변수 : 함수 안에서 만들어진 변수
           # 함수 안에서만 접근이 가능.

func1()
# print(a)

# 전역변수 : 함수 밖에서 만들어진 변수
# 모든 지역에서 접근이 가능 (read-only)
num = 10

def func2():
    global num # 전역변수 num 의 값 수정 허락맡기
    num += 1
    print(num)
func2()