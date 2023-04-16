# generator 공부 : https://dojang.io/mod/page/view.php?id=2412

# ● 발생자(generator)
    # 1. 개념 : 간단 iterator(값을 차례대로 꺼낼 수 있는 객체(object))
    # 2. 특징
        # 1) generator 반환 by yield 지정값
        # 2) iterator 예외 발생 by 자동

    # 3. 사용방법
        # 1) generator 생성 : 함수 내에서 yield 이용하면 generator가 된다
            # - yield
                # 반복문 따로 필요 + 변수 저장. 이 값이 __next__ 메서드의 반환값으로 yield값 순서대로 출력
                    # 변수를 함수 바깥으로 전달하고, 잠시 함수 바깥에서 코드 실행되었다가, 다시 함수 복귀
            # - return
                # 변수 저장x
                    # 변수를 함수 바깥으로 전달하고, 즉시 함수 끝냄
            # - yield from iterable
            # - yield from iterator
            # - yield from generator
                # 반복문 따로 필요x + 변수 저장. 이 값이 __next__ 메서드의 반환값으로 yield값 순서대로 출력
                    # 변수를 함수 바깥으로 전달하고, 잠시 함수 바깥에서 코드 실행되었다가, 다시 함수 복귀
        # 2) generator 사용
            # (1) for문의 반복 : for i in generator_def_name(n):
            # (1) iterator 언패킹 : a, b, c = generator_def_name(n)

print('ㅡㅡㅡㅡㅡㅡㅡgenerator 생성 - for문xㅡㅡㅡㅡㅡㅡㅡ')
def number_generator():
    yield 0 # 0을 함수 바깥으로 전달하고, 잠시 함수 바깥에서 코드 실행되었다가, 다시 함수 복귀
    yield 1 # 1을 함수 바깥으로 전달하고, 잠시 함수 바깥에서 코드 실행되었다가, 다시 함수 복귀
    yield 2 # 2을 함수 바깥으로 전달하고, 잠시 함수 바깥에서 코드 실행되었다가, 다시 함수 복귀

for i in number_generator():
    print(i)

# 예외 발생시에 바로 종료되서 주석으로 해둠. 안 뭉탱이씩 주석 풀고 나머지는 전부 주석해서 테스트
print('ㅡㅡㅡㅡㅡㅡㅡgenerator가 iterator인지 확인 - for문xㅡㅡㅡㅡㅡㅡㅡ')
g = number_generator()
print('객체의 메서드 확인 : {}'.format(dir(g)))
print('gererator 객체인지 식별 : {}'.format(g))

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) # 예외 발생

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # 예외 발생

print('ㅡㅡㅡㅡㅡㅡㅡgenerator2 생성 - for문ㅡㅡㅡㅡㅡㅡㅡ')
def number_generator2(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

for i in number_generator2(3):
    print(i)

# 예외 발생시에 바로 종료되서 주석으로 해둠. 안 뭉탱이씩 주석 풀고 나머지는 전부 주석해서 테스트
print('ㅡㅡㅡㅡㅡㅡㅡgenerator2가 iterator인지 확인 - for문ㅡㅡㅡㅡㅡㅡㅡ')
g = number_generator2(3)
print('객체의 메서드 확인 : {}'.format(dir(g)))
print('gererator 객체인지 식별 : {}'.format(g))

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) # 예외 발생

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # 예외 발생

print('ㅡㅡㅡㅡㅡㅡㅡgenerator3 생성 - yield의 함수호출ㅡㅡㅡㅡㅡㅡㅡ')
def upper_generator(x):
    for i in x:
        yield i.upper() # 함수의 반환값을 바깥으로 전달

fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)

print('ㅡㅡㅡㅡㅡㅡㅡgenerator4 생성 - yield fromㅡㅡㅡㅡㅡㅡㅡ')
def number_generator4():
    x = [1, 2, 3]
    yield from x # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달

for i in number_generator4():
    print(i)

# 예외 발생시에 바로 종료되서 주석으로 해둠. 안 뭉탱이씩 주석 풀고 나머지는 전부 주석해서 테스트
print('ㅡㅡㅡㅡㅡㅡㅡgenerator4가 iterator인지 확인 - yield fromㅡㅡㅡㅡㅡㅡㅡ')
g = number_generator4()
print('객체의 메서드 확인 : {}'.format(dir(g)))
print('gererator 객체인지 식별 : {}'.format(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # 예외 발생

print('ㅡㅡㅡㅡㅡㅡㅡgenerator5 생성 - yield from 숫자 여러번 바깥 전달ㅡㅡㅡㅡㅡㅡㅡ')
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3) # 숫자를 3번 바깥으로 전달

for i in three_generator():
    print(i)