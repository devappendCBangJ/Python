# __init__에서 패키지만 불러와도, 모듈의 변수 함수 클래스 자동으로 불러오게 설정한 예제
    # - from 패키지명 import 모듈명 -> 함수 바로 사용 가능

from calcpkg import *           # 패키지폴더의 __init__.py파일에 모듈의 함수를 불러오는 코드가 있으므로, 함수를 불러오지 않고 calcpkg 패키지의 모듈만 가져와도 ㄱㅊ

print(add(10, 20))              # operation 모듈의 add 함수
print(mul(10, 20))              # operation 모듈의 mul 함수

print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수