# iter, next 공부 : https://dojang.io/mod/page/view.php?id=2405

# ● 반복 가능한 객체(iterable)
    # 1. 개념 : 반복할 수 있는 객체(object)
    # 2. 특징
        # 1) 요소가 여러개 들어있고, 한번에 하나씩 꺼낼 수 있는 객체
        # 2) 구성
            # 반복 가능한 객체
                # 시퀀스 객체 : 요소의 순서가 정해져 있음
                    # ex. 문자열, 리스트, 튜플, range
                # 시퀀스 객체x : 요소의 순서가 정해져있지 않음
                    # ex. 딕셔너리, 세트
    # 3. 사용방법
        # 1) 특징 출력
            # (1) 객체의 메서드 확인 : dir(변수 or 객체)
            # (1) 객체가 반복 가능한 객체인지 식별 : 객체.__iter__()
        # 2) iterable 사용
            # (1) 객체 요소 차례대로 꺼내기 : 객체.__iter__().__next__()
                # - 꺼낼 요소 없어지면 StopIteration 예외 발생하여 반복 끝냄
            # (1) for문 반복 : for i in range(n)
                # 사용시 해당 변수에 __iter__로 iterator를 얻음
                # >> 한 번 박복할때마다 __next__로 다음 숫자 꺼내서 i에 저장
                # >> 지정된 숫자가 n이 되면 StopIteration 발생하여 반복 끝

print('ㅡㅡㅡㅡㅡㅡㅡiterable 배열ㅡㅡㅡㅡㅡㅡㅡ')
print(dir([1, 2, 3]))
print([1, 2, 3].__iter__())
print([1, 2, 3].__iter__().__next__())


print('ㅡㅡㅡㅡㅡㅡㅡiterable 문자열ㅡㅡㅡㅡㅡㅡㅡ')
print('Hello Word!'.__iter__())
print({'a':1, 'b':2}.__iter__())
print({1, 2, 3}.__iter__())

print('ㅡㅡㅡㅡㅡㅡㅡiterable rangeㅡㅡㅡㅡㅡㅡㅡ')
print(range(3).__iter__())
print(range(3).__iter__().__next__())
print(range(3).__iter__().__next__())
print(range(3).__iter__().__next__())

# ● 반복자(iterator)
    # 1. 개념 : 값을 차례대로 꺼낼 수 있는 객체(object)
    # 2. 특징
        # 1) 지연 평가(iterator만 미리 생성, 필요한 시점이 되었을때 데이터 생성)
        # 2) iterator 반환 by __next__ 메서드
        # 2) iterator 예외 발생 by raise
    # 3. 사용방법
        # 1) iterator class 생성 by __iter__, __next__
        # 1) iterator class 생성 by __getitem__
        # 2) iterator 사용
            # (1) for문의 반복 : for i in iterator_class_name(n):
            # (1) iterator 언패킹 : a, b, c = iterator_class_name(n)

# ● iter함수, next함수 :
    # 1) iter 함수 : __iter__ 메서드 호출
        # iter(호출가능한 객체, 반복을 끝낼값)
            # - 반복 끝낼값이 안나왔을 때 : 해당값 출력
            # - 반복 끝낼값이 나왔을 때 : 종료
    # 2) next 함수 : __next__ 메서드 호출
        # next(반복 가능한 객체, 기본값)
        # next(iter(호출가능한 객체, 반복을 끝낼값), 기본값)
            # - 반복 가능할 때 : 해당값 출력
            # - 반복 끝났을 때 : 기본값 출력

print('ㅡㅡㅡㅡㅡㅡㅡiterator class 생성 by __iter__, __next__ㅡㅡㅡㅡㅡㅡㅡ')
class Counter:
    # 초기값 선언
    def __init__(self, stop):
        self.current = 0 # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop # 반복을 끝낼 숫자

    # 반복 가능한 객체(iterable) 생성
    def  __iter__(self):
        return self # 현재 인스턴스 반환

    # 반복자(iterator) 생성
    def __next__(self):
        if self.current < self.stop: # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current # 현재 숫자를 변수에 저장
            self.current += 1 # 현재 숫자 1 증가
            return r # 숫자 반환
        else: # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration # 예외 발생

for i in Counter(3):
    print(i, end=' ')
print()

print('ㅡㅡㅡㅡㅡㅡㅡiterator class2 생성 by __getitem__ㅡㅡㅡㅡㅡㅡㅡ')
class Counter2:
    # 초기값 선언
    def __init__(self, stop):
        self.stop = stop # 반복을 끝낼 숫자

    # 반복 가능한 객체(iterable) + 반복자(iterator) 생성
    def __getitem__(self, index): # 인덱스 받음
        if index < self.stop: # 인덱스가 반복을 끝낼 숫자보다 작을 때
            return index*10 # 인덱스 반환
        else: # 인덱스가 반복을 끝낼 숫자보다 크거나 같을 때
            raise IndexError # 예외 발생

print(Counter2(3)[0], Counter2(3)[1], Counter2(3)[2])

for i in Counter2(3):
    print(i, end=' ')
print()

print('ㅡㅡㅡㅡㅡㅡㅡiterator unpackingㅡㅡㅡㅡㅡㅡㅡ')
a, b, c = Counter(3)
print(a, b, c)

a, b, c, d, e = Counter(5)
print(a, b, c, d, e)

# 예외 발생시에 바로 종료되서 주석으로 해둠. 안 뭉탱이씩 주석 풀고 나머지는 전부 주석해서 테스트
print('ㅡㅡㅡㅡㅡㅡㅡiterator iter, nextㅡㅡㅡㅡㅡㅡㅡ')
import random

# it = iter(range(3))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # range를 벗어나서 예외 발생

# it = iter(lambda : random.randint(0, 5), 2)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # range를 벗어나서 예외 발생

# for i in iter(lambda : random.randint(0, 5), 2): # random된 수를 계속 뽑다가 2가 나오면 멈춰
#     print(i, end=' ')
#
# while True: # random된 수를 계속 뽑다가 2가 나오면 멈춰
#     i = random.randint(0, 5)
#     if i==2:
#         break
#     print(i, end=' ')

it = iter(range(3))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))