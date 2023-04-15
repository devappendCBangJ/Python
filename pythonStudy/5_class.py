# 클래스 공부 : https://dojang.io/mod/page/view.php?id=2372
# 클래스 공부 : https://dojang.io/mod/page/view.php?id=2378

# ● 객체지향(object oriented) 프로그래밍
    # 1. 개념 : 복잡한 문제 >> 잘게 나눈 문제 >> 객체로 만듦 >> 객체 조합 >> 문제 해결
    # 2. 특징
        # - 복잡한 문제 해결 편의성
        # - 개선, 발전 효율적
        # - 유지, 보수 효율적

# ● class
    # 1. 개념 : 객체를 생성 붕어빵 틀
        # 1) 객체(object) : 기사, 마법사, 궁수, 사제, 집, 자동차, 나무, 스크롤바, 버튼, 체크박스 등 특정 개념 or 모양
            # - 인스턴스와 같은 개념 but 객체만 지칭할때 객체라고 부름
            # ex. a = list(range(10))에서 a 자체만 놓고보면 객체임
        # 1) 인스턴스(instance) :
            # - 객체와 같은 개념 but 클래스와 연관지어서 말할때 인스턴스라고 부름
            # ex. a = list(range(10))에서 a는 list클래스의 인스턴스임
        # 2) 클래스(class) : 객체를 생성하는 붕어빵 틀
            # ex. int(), list(), dict()등 자료형도 클래스임
        # 3) 속성(attribute) : 체력, 마나, 물리 공격력, 주문력 등 데이터
            # (0) 인스턴스 속성 : 인스턴스별로 속성 독립. 각 인스턴스가 다른 값을 저장해야할 때 사용
                # - self.속성명 : 클래스 외부 호출 및 변경 가능 속성. 반드시 __init__메서드 안에 생성
                # - self.__속성명 : 클래스 외부 호출 및 변경 불가 속성. 반드시 __init__메서드 안에 생성
            # (1) class 속성 : 모든 인스턴스가 속성 공유. 인스턴스 전체가 같은 값을 공유해야할 때 사용
                # 속성명 : 클래스 외부 호출 및 변경 가능 속성. __init__메서드 안이 아닌 class 바로 안쪽에서 생성
                # __속성명 : 클래스 외부 호출 및 변경 불가 속성. __init__메서드 안이 아닌 class 바로 안쪽에서 생성
        # 4) 메서드(method) : 베기, 찌르기 등 기능(class 내의 함수)
            # (0) __???__ 메서드 = 매직 메서드 = 스페셜 메서드 : 파이썬이 자동으로 호출해주는 메서드
            # (1) __init__ 메서드 : 인스턴스 생성하는 순간 인스턴스(객체) 초기화
            # (2) 기타 메서드

            # (3) 정적 메서드 : 인스턴스 상태, 외부 상태 변화x 메서드
                # - 인스턴스 속성, 인스턴스 메서드가 필요 없을 경우
                # - self를 받지 않아서 인스턴스 속성에 접근 불가
                # - 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수함수(pure function) 만들때 유용
                # - 순수함수는 부수효과가 없고 입력값이 같으면 언제나 같은 출력값 반환
                # - 정적메서드는 인스턴스의 상태를 변화시키지 않는 메서드를 만들때 사용
            # (4) 클래스 메서드 : self를 cls가 대신한다

            # ex. b = list(~~).append(~~)도 인스턴스의 메서드를 호출한 것임
        # 5) self : self자리에 인스턴스가 대입된다
    # 2. 특징
    # 3. 사용방법
        # 1) class + 인스턴스 메서드
            # class 클래스명:       # 클래스명은 반드시 대문자 시작
                # def 메서드명(self):       # 메서드명의 첫번째 매개변수는 반드시 self
                    # 코드들
                # def...
        # 1) class + 인스턴스 attribute 생성(+ 인스턴스 초기화)
            # class 클래스명:
                # def __init__(self):       # 인스턴스를 생성하는 순간 인스턴스(객체) 초기화
                    # self.속성명 = 값      # 인스턴스별로 속성 독립. 각 인스턴스가 다른 값을 저장해야할 때 사용(클래스 외부 호출 및 변경 가능 속성. 반드시 __init__메서드 안에 생성)
        # 1) class + 인스턴스 attribute 생성(+ 인스턴스 초기화) & 매개변수 값 받기
            # class 클래스명:
                # def __init__(self, 매개변수1, 매개변수2)
                    # self.속성명1 = 매개변수1
                    # self.속성명2 = 매개변수2
        # 1) class + 비공개 인스턴스 attribute 생성
            # class 클래스명:
                # def __init__(self):
                    # self.__속성 = 값       # 인스턴스별로 속성 독립. 각 인스턴스가 다른 값을 저장해야할 때 사용(클래스 외부 호출 및 변경 불가 속성. 반드시 __init__메서드 안에 생성)
        # 1) class + class attribute 생성
            # class 클래스명:
                # 속성명 = 값        # 모든 인스턴스가 속성 공유. 인스턴스 전체가 같은 값을 공유해야할 때 사용(클래스 외부 호출 및 변경 가능 속성. __init__메서드 안이 아닌 class 바로 안쪽에서 생성)
        # 1) class + 비공개 class attribute 생성
            # class 클래스명:
                # __속성명 = 값     # 모든 인스턴스가 속성 공유. 인스턴스 전체가 같은 값을 공유해야할 때 사용(클래스 외부 호출 및 변경 불가 속성. __init__메서드 안이 아닌 class 바로 안쪽에서 생성)
        # 2) class 사용
            # (1) 인스턴스 생성 : 인스턴스명 = 클래스명()
            # (2) 인스턴스 메서드 호출 : 인스턴스명.메서드명()
            # (3) 인스턴스 속성 호출 : 인스턴스명.속성명
                # 1] 코드 동작 순선
                    # [1] 인스턴스명.속성명이 있는가? 판단
                        # - 예 >> 인스턴스명.속성명 호출
                        # - 아니요 >> 클래스명.속성명이 있는가? 판단
                            # - 예 >> 클래스명.속성명 호출
                            # - 아니요 >> Attribute 에러 발생
            # (3) 클래스 속성 호출 : 클래스명.속성명 or 인스턴스명.속성명
            

        # 1) class + 정적 메서드
            # class 클래스명:
                # @staticmethod     # 인스턴스 정의x, 인스턴스 상태x, 외부 상태 변화x 메서드
                # def 메서드명(매개변수1, 매개변수2):
                    # 코드
        # 2) class 사용
            # (1) 정적 메서드 사용 : 클래스명.메서드명()


        # 1) class + 클래스 메서드
            # class 클래스명:
                # @classmethod        # self를 cls가 대신한다
                # def 메서드명(cls, 매개변수1, 매개변수2):
                    # 코드
        # 2) class 사용
            # (1) 인스턴스 생성 : 인스턴스명 = 클래스명()
            # (2) 클래스 메서드 호출 : 클래스명.메서드명()

print('ㅡㅡㅡㅡㅡㅡㅡclass + 인스턴스 메서드ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def greeting(self):
        print('Hello')
# 인스턴스 생성
james = Person()
# 인스턴스 메서드 호출
james.greeting()

print('ㅡㅡㅡㅡㅡㅡㅡclass 사용 예시ㅡㅡㅡㅡㅡㅡㅡ')
# 인스턴스 생성
a = int(10)
print(a)
print(type(a))

# 인스턴스 생성
b = list(range(10))
# 인스턴스 메서드 호출
b.append(20)
print(b)
print(type(b))

# 인스턴스 생성
c = dict(x=10, y=20)
print(c)
print(type(c))

# 인스턴스 생성
maria = Person()
print(type(maria))

print('ㅡㅡㅡㅡㅡㅡㅡclass + attribute(+ 인스턴스 초기화)ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self):
        self.hello = "안녕하세요."

    def greeting(self):
        print(self.hello)

# 인스턴스 생성
james = Person()
# 인스턴스 메서드 호출
james.greeting()

print('ㅡㅡㅡㅡㅡㅡㅡclass + attribute(+ 인스턴스 초기화) & 매개변수 값 받기ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕하세요."
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

# 인스턴스 생성
maria = Person('마리아', 20, '서울시 서초구 반포동')
# 인스턴스 메서드 호출
maria.greeting()
# 인스턴스 속성 호출
print('인사 : ', maria.hello)
print('이름 : ', maria.name)
print('나이 : ', maria.age)
print('주소 : ', maria.address)

print('ㅡㅡㅡㅡㅡㅡㅡclass + 비공개 attributeㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount     # 클래스 내부에서 비공개 속성 접근 가능
        print('이제 {0}원 남았네요.'.format(self.__wallet))

# 인스턴스 생성
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# 인스턴스 비공개 속성 호출
# maria.__wallet -= 10000     # 클래스 바깥에서 비공개 속성 접근 불가. 에러 발생
maria.pay(3000)

print('ㅡㅡㅡㅡㅡㅡㅡclass + 비공개 attribute2ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        if amount > self.__wallet:
            print('얼마 남았는지는 기밀이지만, 돈이 모자릅니다.')
            return
        self.__wallet -= amount

# 인스턴스 생성
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# 인스턴스 비공개 속성 호출
# maria.__wallet -= 10000     # 클래스 바깥에서 비공개 인스턴스 속성 접근 불가. 에러 발생
maria.pay(10001)

print('ㅡㅡㅡㅡㅡㅡㅡclass 연습문제1ㅡㅡㅡㅡㅡㅡㅡ')
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()

print('ㅡㅡㅡㅡㅡㅡㅡclass + class attributeㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    bag = []

    def put_bag(self, stuff):
        # self.bag.append(stuff)      # self : 인스턴스를 의미. 이렇게 해도 되지만 코드 가독성이 모호해진다
        Person.bag.append(stuff)        # 클래스명 : 클래스를 의미. 이렇게 하면 코드가 명확해진다

# 인스턴스 생성
james = Person()
# 인스턴스 메서드 호출
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')
# 인스턴스 속성 호출
print(james.bag)
print(maria.bag)
# 클래스 속성 호출
print(Person.bag)

print('ㅡㅡㅡㅡㅡㅡㅡclass + class attribute X, instance attribute Oㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)
        
# 인스턴스 생성
james = Person()
# 인스턴스 메서드 호출
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

# 인스턴스 속성 호출
print(james.bag)
print(maria.bag)
# 클래스 속성 호출
# print(Person.bag)       # 클래스 속성은 없으므로 에러 발생

print('ㅡㅡㅡㅡㅡㅡㅡclass + 비공개 class attributeㅡㅡㅡㅡㅡㅡㅡ')
class Knight:
    __item_limit = 10

    def print_item_limit(self):
        print(Knight.__item_limit)

# 인스턴스 생성
x = Knight()
# 인스턴스 메서드 호출
x.print_item_limit()
# 클래스 속성 호출
# print(Knight.__item_limit)     # 클래스 바깥에서 비공개 클래스 속성 접근 불가. 에러 발생

print('ㅡㅡㅡㅡㅡㅡㅡclass + 정적 메서드ㅡㅡㅡㅡㅡㅡㅡ')
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

# 정적 메서드 호출
Calc.add(10, 20)
Calc.mul(10, 20)

print('ㅡㅡㅡㅡㅡㅡㅡclass + 클래스 메서드ㅡㅡㅡㅡㅡㅡㅡ')
class Person:
    count = 0

    def __init__(self):
        # self.count      # self : 인스턴스를 의미. 이렇게 해도 되지만 코드 가독성이 모호해진다
        Person.count += 1       # 클래스명 : 클래스를 의미. 이렇게 하면 코드가 명확해진다

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))        # cls로 클래스 속성에 접근

    @classmethod
    def create(cls):
        p = cls()       # ● cls()로 인스턴스 생성 ●
        return p

# 인스턴스 생성
james = Person()
maria = Person()
# 인스턴스 메서드 호출
maria.print_count()
# 클래스 메서드 호출
Person.print_count()

print('ㅡㅡㅡㅡㅡㅡㅡclass 연습문제2ㅡㅡㅡㅡㅡㅡㅡ')      # ♣
class Date:
    @staticmethod
    def is_data_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

if Date.is_data_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')
    # 클래스에 접근할 필요가 없으므로 정적 메서드로 생성
    # 월이 12월 이하이면서, 일이 31일 이하인지 검사
    # 만족하면 True 반환, 만족하지 않으면 False 반환