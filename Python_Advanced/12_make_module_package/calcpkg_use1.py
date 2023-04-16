# __init__에서 아무것도 작성하지 않았을때의 예제
    # - import 패키지명.모듈명 -> 패키지명.모듈명.변수 or 함수 or 클래스 사용 가능

import calcpkg.operation  # 패키지폴더의 __init__.py파일에 모듈을 불러오는 코드가 있으므로, 모듈을 불러오지 않고 calcpkg 패키지만 가져와도 ㄱㅊ긴함
import calcpkg.geometry  # 패키지폴더의 __init__.py파일에 모듈을 불러오는 코드가 있으므로, 모듈을 불러오지 않고 calcpkg 패키지만 가져와도 ㄱㅊ긴함

print(calcpkg.operation.add(10, 20))
print(calcpkg.operation.mul(10, 20))

print(calcpkg.geometry.triangle_area(30, 40))
print(calcpkg.geometry.rectangle_area(30, 40))