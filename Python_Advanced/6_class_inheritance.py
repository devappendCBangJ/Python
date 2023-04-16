# 클래스 상속 공부 : https://dojang.io/mod/page/view.php?id=2384

# ● 클래스 상속(class inheritance) + 메서드 오버라이딩(method overriding)
    # 1. 개념 : 기반 클래스의 기능을 유지한 채로 상속 받아, 파생 클래스가 다른 기능을 추가할 때 사용하는 기능
        # - 기반 클래스(base class) : 파생 클래스에게 기능 상속해줌
            # = 부모 클래스(parent class) = 슈퍼 클래스(super class)
        # - 파생 클래스(derived class) : 기반 클래스에게 기능 상속받고, 새로운 클래스 생성
            # = 자식 클래스(child class) = 서브 클래스(sub class)
    # 2. 특징
        # 1) 클래스 상속
            # - 기반 클래스 기능을 파생 클래스에 재활용하므로 효율적
            # - 파생 클래스가 기반 클래스 안에 포함되거나 동등한 개념일때 유용하다
            # (1) 다중 상속
            # (2) 다이아몬스 상속
        # 2) 메서드 오버라이딩
            # - 우선순위 : 파생 클래스 > 기반 클래스
            # - 같은 메서드 이름으로 계속 어떤 기능이 사용되어야할 때 사용
            # - 중복되는 기능은 super로 기반 클래스 기능을 재사용하면 효율적
    # 3. 사용방법
        # 1) 기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 불가
            # class 기반클래스명:
                # 코드
            # class 파생클래스명(기반클래스명):     # 기반 클래스 기능을 파생 클래스에 상속
                # 코드
        # 1) 기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 1way
            # class 기반클래스명:
                # 코드
            # class 파생클래스명(기반클래스명):
                # super().기반 클래스의 메서드명()        # 기반 클래스의 메서드 호출
                # 코드
        # 1) 기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 2way
            # class 기반클래스명:
                # 코드
            # class 파생클래스명(기반클래스명):
                # pass      # 파생 클래스에 __init__메서드가 없으면 기반 클래스의 __init__메서드 자동 호출
        # 1) 기반 + 파생 class + 포함관계(포함방식 사용)
            # class 기반클래스명:     # 기반 클래스 기능을 파생 클래스에 포함
                # 코드
            # class 파생클래스명():
                # def __init__(self):
                    # self.속성명 = []     # 리스트 속성에 기반 클래스 인스턴스를 넣어서 관리
                # def 메서드명(self, 매개변수1):
                    # self.속성명.append(매개변수1)        # 리스트 속성에 기반 클래스 인스턴스를 추가하는 함수
        # 1) 기반 + 파생 class + 동등관계(상속방식 사용) + 메서드 오버라이딩
            # class 기반클래스명:
                # def 파생클래스와 동일한 메서드명(self):
                    # 코드
            # class 파생클래스명(기반클래스명):
                # def 기반클래스와 동일한 메서드명(self):        # 메서드오버라이딩 : 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할때 사용
                    # 코드
        # 1) 기반 + 파생 class + 동등관계(상속방식 사용) + 메서드 오버라이딩 + 기반 클래스 속성 사용
            # class 기반클래스명:
                # def 파생클래스와 동일한 메서드명(self):
                    # 코드
            # class 파생클래스명(기반클래스명):
                # def 기반클래스와 동일한 메서드명(self):        # 메서드오버라이딩 : 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할때 사용
                    # super().파생클래스와 동일한 메서드명()
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

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용)ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('안녕하세요.')
        
class Student(Person):
    def study(self):
        print('공부하기.')

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
james.greeting()        # 기반 클래스 Person의 메서드 호출
james.study()       # 파생 클래스 Student에 추가한 메서드 호출

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 포함관계(포함방식 사용)ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList():
    def __init__(self):
        self.person_list = []       # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):        # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

# james = Person()
# PersonList.append_person(james)
# print(PersonList.person_list[0])
# 이렇게 하면 안되네??? 사용을 어캐하지???

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 불가ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장.'

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
print(james.school)
# print(james.hello)        # 파생 클래스의 인스턴스 생성 시에 기반 클래스인 Person의 __init__이 호출되지 않아서 self.hello 속성이 생성되지 않고, 이로 인해 오류 발생

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 1wayㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()      # super() : 기반 클래스의 __init__메서드 호출
        self.school = '파이썬 코딩 도장.'

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
print(james.school)
print(james.hello)        # 파생 클래스의 인스턴스 생성 시에 기반 클래스인 Person의 __init__이 super().__init__()으로 호출되어 self.hello 속성이 생성됨

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용) + 기반 클래스 속성 사용 2wayㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
print(james.hello)        # 파생 클래스의 인스턴스 생성 시에 기반 클래스인 Person의 __init__ 자동 호출되어 self.hello 속성이 생성됨

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용) + 메서드 오버라이딩ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
james.greeting()

print('ㅡㅡㅡㅡㅡㅡㅡ기반 + 파생 class + 동등관계(상속방식 사용) + 메서드 오버라이딩 + 기반 클래스 속성 사용ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()      # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# 인스턴스 생성
james = Student()
# 인스턴스 메서드 호출
james.greeting()