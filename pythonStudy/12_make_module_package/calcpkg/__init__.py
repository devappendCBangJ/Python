
# 1. 사용법
    # 1) __init__.py 파일 비워두기
    # 1) 패키지만 불러와도, 모듈 자동으로 불러오게 설정
        # from . import 모듈명1, 모듈명2, ...
    # 1) 패키지만 불러와도, 모듈의 변수 함수 클래스 자동으로 불러오게 설정
        # from .모듈명 import 변수, 함수, 클래스, ...
    # 1) 패키지만 불러와도, 모듈의 모든 변수 함수 클래스 자동으로 불러오게 설정
        # from .모듈명 import *

# 패키지만 불러와도, 모듈 자동으로 불러오게 설정
from . import geometry
from . import operation

# 패키지만 불러와도, 모듈의 변수 함수 클래스 자동으로 불러오게 설정
from .operation import add, mul
from .geometry import triangle_area, rectangle_area

# 패키지만 불러와도, 모듈의 모든 변수 함수 클래스 자동으로 불러오게 설정
from .operation import *
from .geometry import *