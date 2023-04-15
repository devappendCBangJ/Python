# lambda 공부 : https://dojang.io/mod/page/view.php?id=2359

# ● 람다 표현식(lambda expression)
    # 1. 개념 : 익명함수(이름 없이 간단히 만드는 함수)
    # 2. 특징
        # 1) lambda 표현식 안에서 새로운 변수 생성 불가 - def함수로 작성
        # 2) lambda 표현식 바깥의 변수 사용 가능

    # 3. 사용방법
        # 1) lambda 생성 + 사용 : (lambda 매개변수 : 반환값)(n)
        # 1) lambda 생성 : 익명 함수 변수 = lambda 매개변수 : 반환값
        # 2) lambda 사용 : 익명 함수 변수(n)
        # 2) lambda 사용 + map 1개 매개변수, 인수 : list(map(lambda 매개변수1 : 반환값, iterable))
        # 2) lambda 사용 + map 여러 매개변수, 인수 : list(map(lambda 매개변수1, 매개변수2, ... : 반환값, iterable1, iterable2, ...))
        # 2) lambda 사용 + map + 조건부 표현식 : list(map(lambda 매개변수 : 조건1일때_반환값 if 조건1 else 그외경우_반환값, iterable))
        # 2) lambda 사용 + map + 여러 조건부 표현식 : list(map(lambda 매개변수 : 조건1일때_반환값 if 조건1 else 조건2일때_반환값 if 조건2 else 그외경우_반환값, iterable))
            # - 주의사항
                # if와 else에 콜론 사용x
                # if와 else를 함께 사용
                # if만 독립적으로 사용 불가
                # elif 사용 불가
                # 조건부 표현식이 너무 길어지면 def함수로 작성하는 것이 효율적
        # 3) lambda 사용 + filter :

print('ㅡㅡㅡㅡㅡㅡㅡ일반 함수ㅡㅡㅡㅡㅡㅡㅡ')
def plus_ten(x):
    return x + 10

print(plus_ten(1))

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 생성ㅡㅡㅡㅡㅡㅡㅡ')
plus_ten = lambda x: x+10
print(lambda x: x+10)
print(plus_ten(1))

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 생성 + 사용ㅡㅡㅡㅡㅡㅡㅡ')
print(lambda x: x+10)
print((lambda x: x+10)(1))

# 동작 되는 코드라서 주석처리 안해둠
y = 10
print((lambda x: x+y)(1))

# 동작하지 않는 코드라서 주석처리 해둠
# print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 생성 + 사용ㅡㅡㅡㅡㅡㅡㅡ')
# print(lambda x: y = 10; x + y)(1)

print('ㅡㅡㅡㅡㅡㅡㅡ일반함수를 인수로 사용ㅡㅡㅡㅡㅡㅡㅡ')
def plus_ten2(x):
    return x + 10
b = list(map(plus_ten2, [1, 2, 3]))
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식을 인수로 사용ㅡㅡㅡㅡㅡㅡㅡ')
b = list(map(lambda x: x + 10, [1, 2, 3]))
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 + 조건부 표현식ㅡㅡㅡㅡㅡㅡㅡ')
a = [1, 2, 3,4 ,5 ,6, 7, 8, 9, 10]
b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ일반함수 + 여러 조건부 표현식ㅡㅡㅡㅡㅡㅡㅡ')
a = [1, 2, 3,4 ,5 ,6, 7, 8, 9, 10]
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
b = list(map(f, a))
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 + 여러 조건부 표현식ㅡㅡㅡㅡㅡㅡㅡ')
a = [1, 2, 3,4 ,5 ,6, 7, 8, 9, 10]
b = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡlambda 표현식 + map 여러 객체ㅡㅡㅡㅡㅡㅡㅡ')
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))