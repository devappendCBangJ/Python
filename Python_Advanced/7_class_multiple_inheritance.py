# 클래스 다중 상속 공부 : https://dojang.io/mod/page/view.php?id=2388

# ● 클래스 다중 상속(class multiple inheritance)
    # 1. 개념 : 여러 기반 클래스의 기능을 유지한 채로 상속 받아, 파생 클래스가 다른 기능을 추가할 때 사용하는 기능
        # - 기반 클래스(base class) : 파생 클래스에게 기능 상속해줌
            # = 부모 클래스(parent class) = 슈퍼 클래스(super class)
        # - 파생 클래스(derived class) : 기반 클래스에게 기능 상속받고, 새로운 클래스 생성
            # = 자식 클래스(child class) = 서브 클래스(sub class)
        # - 추상 클래스 : 메서드의 목록만 가진 클래스. 파생 클래스에서 반드시 구현해야할 메서드 목록 정의
            # (추상 클래스의 메서드는 파생 클래스에서도 정의가 되어있어야한다)
            # 추상클래스는 인스턴스를 만들 수 없다. 상속에만 사용한다.
    # 2. 특징
        # 1) 클래스 상속
            # - 기반 클래스 기능을 파생 클래스에 재활용하므로 효율적
            # - 파생 클래스가 기반 클래스 안에 포함되거나 동등한 개념일때 유용하다
            # (1) 다중 상속
            # (2) 다이아몬드 상속
                # - 문제점 : 메서드 순서가 명확하지 않아서 죽음의 다이아몬드라고 불린다
                # - 해결책 : 메서드 탐색 순서(MRO = Method Resolution Order) 출력하여 확인
        # 2) 메서드 오버라이딩
            # - 우선순위 : 파생 클래스 > 기반 클래스
            # - 같은 메서드 이름으로 계속 어떤 기능이 사용되어야할 때 사용
            # - 중복되는 기능은 super로 기반 클래스 기능을 재사용하면 효율적
    # 3. 사용방법
        # 1) 기반 + 파생 class + 다중 동등관계(다중 상속방식 사용) + 기반 클래스 속성 사용불가
            # class 기반클래스명1:
                # 코드
            # class 기반클래스명2:
                # 코드
            # class 파생클래스명(기반클래스명1, 기반클래스명2):
                # 코드
        # 1) 기반 + 파생 class + 다이아몬드 동등관계(다이아몬드 상속방식 사용) + 기반 클래스 속성 사용불가
            # class 기반클래스명:
                # def 동일 메서드명(self):
                    # 코드
            # class 파생클래스명1(기반클래스명):
                # def 동일 메서드명(self):
                    # 코드
            # class 파생클래스명2(기반클래스명):
                # def 동일 메서드명(self):
                    # 코드
            # class 파생파생클래스명(파생클래스명1, 파생클래스명2):     # 파생파생클래스명의 메서드를 실행하면 파생클래스1의 메서드만 실행된다
                # pass
        # 1) 추상 class
            # from abc import *
            # class 추상클래스명(metaclass=ABCMeta):
                # @abstractmethod
                # def 동일 메서드명(self):
                    # pass
            # class 파생클래스명(추상클래스명):     # 추상 클래스에서 @abstractmethod로 정의된 메서드는 파생클래스에서도 정의되어있어야한다
                # def 동일 메서드명(self):
                    # 코드
        # 2) 기반 + 파생 class 사용
            # (1) 인스턴스 생성 : 인스턴스명 = 클래스명()
            # (2) 인스턴스 메서드 호출 : 인스턴스명.메서드명()
            # (3) 인스턴스 속성 호출 : 인스턴스명.속성명
                # 1] 코드 동작 순서
                    # [1] 인스턴스명.속성명이 있는가? 판단
                        # - 예 >> 인스턴스명.속성명 호출
                        # - 아니요 >> 클래스명.속성명이 있는가? 판단
                            # - 예 >> 클래스명.속성명 호출
                            # - 아니요 >> Attribute 에러 발생
                # 1] 기반 클래스 속성 찾는 코드 동작 순서
                    # [1] 파생 클래스에 인스턴스명.속성명이 있는가? 판단
                        # - 예 >> 파생 클래스의 인스턴스명.속성명 호출
                        # - 아니요 >> 파생 클래스에서 super().__init__()으로 기반 클래스의 __init__이 출력 되었는가? 판단
                            # - 예 >> 기반 클래스의 인스턴스명.속성명 호출
                            # - 아니요 >> Attribute 에러 발생
            # (3) 클래스 속성 호출 : 클래스명.속성명 or 인스턴스명.속성명
            # (4) 클래스의 메서드 탐색 순서(MRO) 출력 : print(클래스명.mro())

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 다중 동등관계(다중 상속방식 사용) + 기반 클래스 속성 사용불가ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리.')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기.')

# 인스턴스 생성
james = Undergraduate()
# 인스턴스 메서드 호출
james.greeting()        # 기반 클래스1 메서드 호출
james.manage_credit()       # 기반 클래스2 메서드 호출
james.study()       # 파생 클래스 메서드 호출

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 다이아몬드 동등관계(다이아몬드 상속방식 사용) + 기반 클래스 속성 사용불가ㅡㅡㅡㅡㅡㅡㅡ')
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass

# 인스턴스 생성
x = D()
# 클래스의 메서드 탐색 순서 출력
print(D.mro())
# 인스턴스 메서드 호출
x.greeting()

print('ㅡㅡㅡㅡㅡㅡㅡ추상 class 오류 verㅡㅡㅡㅡㅡㅡㅡ')
from abc import *

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass
    
class Student(StudentBase):
    def study(self):
        print('공부하기')

# 인스턴스 생성
# james = Student()            # 추상 class에서 @abstractmethod가 붙여진 메서드들은 파생 클래스에도 전부 구현이 되어있어야한다. 인스턴스 생성시 판단하여, 구현 안되어있다면 오류 발생
# 인스턴스 메서드 호출
# james.study()

print('ㅡㅡㅡㅡㅡㅡㅡ추상 class 오류없는 verㅡㅡㅡㅡㅡㅡㅡ')
from abc import *

class StudentBase(metaclass = ABCMeta):     # 추상클래스로 인스턴스 만들기는 불가능. 상속에만 사용. 파생 클래스에서 반드시 구현해야할 메서드 목록 정의
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기.')

    def go_to_school(self):
        print('학교가기.')

james = Student()       # 추상 class에서 @abstractmethod가 붙여진 메서드들은 파생 클래스에도 전부 구현이 되어있어야한다. 인스턴스 생성시 판단하여, 구현 안되어있다면 오류 발생
james.study()
james.go_to_school()

print('ㅡㅡㅡㅡㅡㅡㅡclass inheritance 연습문제 2wayㅡㅡㅡㅡㅡㅡㅡ')
class AdvancedList(list):
    def replace(self, tar, chg):
        for i in range(len(self)):
            if(self[i] == tar):
                self[i] = chg

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

print('ㅡㅡㅡㅡㅡㅡㅡclass inheritance 연습문제 1wayㅡㅡㅡㅡㅡㅡㅡ')
class AdvancedList(list):       # list라는 기반 클래스를 상속받았으므로, 기반 클래스에 있는 모든 메서드 사용 가능
    def replace(self, old, new):
        while old in self:      # 인스턴스 내에 원소값이 old인 것이 있는 동안 반복
            self[self.index(old)] = new     # 원소값이 old인 것의 인덱스를 추출하고, 그 원소값을 new로 취한다

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

