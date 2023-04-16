# <함수 정의>
# def 함수(매개 변수):   : 함수 정의
#   함수 정의
#   return 반환값       : 함수 반환

# <함수 호출>
# 함수(인자)            : 함수 호출

# 함수 정의
def add(a, b):
    c = a + b
    # 함수 반환
    return c

#함수 호출
result = add(10, 20)
print(result)

def sum_and_mul(a,b):
    return a+b, a*b

result1, result2 = sum_and_mul(10, 20)
print(result1)
result = sum_and_mul(10, 30)
print(result)