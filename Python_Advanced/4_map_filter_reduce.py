# map, filter, reduce 공부 : https://dojang.io/mod/page/view.php?id=2359

# map, filter, reduce 차이
    # map : 함수에서 산술 연산
    # filter : 함수에서 관계 연산
    # reduce : 함수에서 누적 산술 연산

# ● map 함수
    # 1. 개념 : 함수 인수 대입 연산 반복 >> 추출된 값 >> 리스트 or 튜플 생성
    # 2. 특징
        # 0) 함수에서 산술 연산
        # 1) 입력 : 반복 가능한 객체
        # 2) 출력 : 반복 가능한 객체를 인수로 넣어 추출된 함수의 출력값
    # 3. 사용방법
        # 1) map 사용 : map(function, iterable) = map(적용시킬 함수, 적용시킬 값들)
            # - function : 함수
            # - iterable : 반복 가능한 객체 ex. 리스트, 튜플...

print('ㅡㅡㅡㅡㅡㅡㅡ일반 함수ㅡㅡㅡㅡㅡㅡㅡ')
myList = [1, 2, 3, 4, 5]

result1 = []
for val in myList:
    result1.append(val + 1)
print(f'result1 : {result1}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수ㅡㅡㅡㅡㅡㅡㅡ')
def add_one(n):
    return n + 1

result2 = list(map(add_one, myList))
print(f'result2 : {result2}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수 예제1ㅡㅡㅡㅡㅡㅡㅡ')
import math

result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(int, 리스트) : {result1}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수 예제2ㅡㅡㅡㅡㅡㅡㅡ')
def func_pow(x):
    return pow(x, 5)

result2 = list(map(func_pow, [1, 2, 3, 4, 5]))
print(f'map(func_pow, 리스트) : {result2}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수 예제3ㅡㅡㅡㅡㅡㅡㅡ')
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(func_ceil, 리스트) : {result3}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수 예제4ㅡㅡㅡㅡㅡㅡㅡ')
def func_mul(x):
    return x * 2

result1 = list(map(func_mul, [5, 4, 3, 2, 1]))
print(f'map(일반함수, 리스트) : {result1}')

print('ㅡㅡㅡㅡㅡㅡㅡmap 함수 예제5 - lambda 표현식ㅡㅡㅡㅡㅡㅡㅡ')
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
print(f'map(lambda함수, 리스트) : {result2}')

# ● filter 함수
    # 1. 개념 : 함수 인수가 함수 내에서 True False 판단 반복 >> True여서 추출된 값 >> 리스트 or 튜플 생성
    # 2. 특징
        # 0) 함수에서 관계 연산
        # 1) 입력 : 반복 가능한 객체
        # 2) 출력 : 반복 가능한 객체를 인수로 넣어 함수 내에서 True로 판단한 경우에서 함수의 출력값
    # 3. 사용방법
        # 1) filter 사용 : filter(function, iterable)
            # - function : 함수
            # - iterable : 반복 가능한 객체 ex. 리스트, 튜플...

print('ㅡㅡㅡㅡㅡㅡㅡfilter 함수ㅡㅡㅡㅡㅡㅡㅡ')
def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
filter1 = list(filter(f, a))
print(f'filter(일반함수, 리스트) : {filter1}')

print('ㅡㅡㅡㅡㅡㅡㅡfilter 함수 - lambda 표현식ㅡㅡㅡㅡㅡㅡㅡ')
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
filter2 = list(filter(lambda x: x > 5 and x < 10, a))
print(f'filter(lambda함수, 리스트) : {filter2}')

# ● reduce 함수
    # 1. 개념 : 함수 인수 누적 대입 연산 반복 >> 누적 추출된 값 >> 리스트 or 튜플 생성
    # 2. 특징
        # 0) 함수에서 누적 산술 연산
        # 1) 입력 : 반복 가능한 객체
        # 2) 출력 : 반복 가능한 객체를 인수로 넣어 누적 추출된 함수의 출력값
    # 3. 사용방법
        # 0) reduce 모듈 불러오기 : from functools import reduce
        # 1) reduce 사용 : reduce(function, iterable)
            # - function : 함수
            # - iterable : 반복 가능한 객체 ex. 리스트, 튜플...

print('ㅡㅡㅡㅡㅡㅡㅡreduce 함수ㅡㅡㅡㅡㅡㅡㅡ')
def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce1 = reduce(f, a)
print(reduce1)

print('ㅡㅡㅡㅡㅡㅡㅡreduce 함수 - lambda 표현식ㅡㅡㅡㅡㅡㅡㅡ')
a = [1, 2, 3, 4, 5]
from functools import reduce
reduce2 = reduce(lambda x, y: x + y, a)
print(reduce2)