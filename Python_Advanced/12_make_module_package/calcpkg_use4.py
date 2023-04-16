# __init__에서 패키지만 불러와도, 모듈의 모든 변수 함수 클래스 자동으로 불러오게 설정한 예제
    # - import 패키지명 -> 패키지.함수 사용 가능(모듈을 거치지 않아도 됨)

import calcpkg

print(calcpkg.add(10, 20))
print(calcpkg.mul(10, 20))

print(calcpkg.traingle_area(30, 40))
print(calcpkg.rectangle_area(30, 40))