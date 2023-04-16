# 클래스 예제 : https://dojang.io/mod/page/view.php?id=2393

print('ㅡㅡㅡㅡㅡㅡㅡclass 예제 - 두 점 사이의 거리ㅡㅡㅡㅡㅡㅡㅡ')
# 모듈 불러오기
import math

# 클래스 생성
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 인스턴스 생성
p1 = Point2D(x = 30, y = 20)
p2 = Point2D(x = 60, y = 50)

print('p1 : {} {}'.format(p1.x, p1.y))
print('p2 : {} {}'.format(p2.x, p2.y))

# 두 점 사이 거리 계산
a = p2.x - p1.x
b = p2.y - p1.y
a = p1.x - p2.x # 위와 같은 방법
b = p1.y - p2.y
c = math.sqrt((a*a) + (b*b))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) # 위와 같은 방법

# 두 점 사이 거리 출력
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡclass 연습문제 - 사각형의 넓이ㅡㅡㅡㅡㅡㅡㅡ')

# 클래스 생성
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

rect = Rectangle(x1=20, y1= 20, x2=40, y2=30)
width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)