# 모듈 불러오기 공부 : https://dojang.io/mod/page/view.php?id=2441

# ● 모듈과 패키지(module, package)
    # 1. 개념
        # 1) 모듈 : 각종 변수, 함수, 클래스 담은 스크립트 파일
        # 1) 패키지 : 여러 모듈을 묶은 것
    # 2. 특징
        # - 기본 모듈과 패키지 : 파이썬 설치 시, 다양한 모듈과 패키지가 기본으로 설치
        # - 사용자 지정 모듈과 패키지 : 기본 모듈과 패키지가 부족하면, 다른 사람들이 만든 유명 모듈과 패키지 설치해서 사용

        # - pip : 패키지 관리 명령어 in 파이썬 패키지 인덱스
    # 3. 사용방법
        # 1) 모듈 불러오기 : import 모듈1, 모듈2, ...
        # 1) 모듈 불러오기 + 별명 지정 : import 모듈 as 별명

        # 1) 모듈에서 변수 불러오기 : from 모듈 import 변수1, 변수2, ...
        # 1) 모듈에서 변수 불러오기 + 별명 지정 : from 모듈 import 변수 as 별명

        # 1) 모듈에서 함수 불러오기 : from 모듈 import 함수1, 함수2, ...
        # 1) 모듈에서 함수 불러오기 + 별명 지정 : from 모듈 import 함수 as 별명

        # 1) 모듈에서 클래스 불러오기 : from 모듈 import 클래스1, 클래스2, ...
        # 1) 모듈에서 클래스 불러오기 + 별명 지정 : from 모듈 import 클래스 as 별명

        # 1) 모듈에서 일부 불러오기 + 별명 지정 : from 모듈 import 변수 as 별명, 함수 as 별명, 클래스 as 별명, ...
        # 1) 모듈에서 전부 불러오기 : from 모듈 import *

        # 0) 패키지 설치
            # (1) pip 설치
                # - pip도 모듈의 일종이다
                # 1] 윈도우 : Windows용 파이썬에 기본 내장
                # 1] 리눅스, macOS : 터미널(콘솔)에서 설치
                    # curl -O https://bootstrap.pypa.io/get-pip.py
                    # sudo python get-pip.py
            # (2) 패키지 설치 by pip
                # 1] 윈도우
                    # [1] 1way : 명령 프롬프트 실행 - pip install 패키지명
                    # [1] 2way : 명령 프롬프트 실행 - python -m pip install 패키지명
                        # - python에 -m 옵션 지정해서 pip 실행
                        # - -m 옵션 : 모듈을 실행하는 옵션
                # 1] 리눅스, macOS
                    # [1] 1way : 터미널(콘솔) 실행 - sudo pip install 패키지명
                    # [1] 2way : 터미널(콘솔) 실행 - sudo python3 -m pip install 패키지명
                        # - python에 -m 옵션 지정해서 pip 실행
                        # - -m 옵션 : 모듈을 실행하는 옵션

        # 1) 패키지 불러오기 : import 패키지.모듈1, 패키지.모듈2, ...
        # 1) 패키지 불러오기 + 별명 지정 : import 패키지.모듈 as 별명

        # 1) 패키지에서 변수 불러오기 : from 패키지.모듈 import 변수1, 변수2, ...
        # 1) 패키지에서 변수 불러오기 + 별명 지정 : from 패키지.모듈 import 변수 as 별명

        # 1) 패키지에서 함수 불러오기 : from 패키지.모듈 import 함수1, 함수2, ...
        # 1) 패키지에서 함수 불러오기 + 별명 지정 : from 패키지.모듈 import 함수 as 별명

        # 1) 패키지에서 클래스 불러오기 : from 패키지.모듈 import 클래스1, 클래스2, ...
        # 1) 패키지에서 클래스 불러오기 + 별명 지정 : from 패키지.모듈 import 클래스 as 별명

        # 1) 패키지에서 일부 불러오기 + 별명 지정 : from 패키지.모듈 import 변수 as 별명, 함수 as 별명, 클래스 as 별명, ...
        # 1) 패키지에서 전부 불러오기 : from 패키지.모듈 import *

        # 2) 모듈 사용
            # (1) 모듈.변수
            # (1) 모듈.함수()
            # (1) 모듈.클래스()

        # 2) 패키지 사용
            # (1) 패키지.모듈.변수
            # (1) 패키지.모듈.함수()
            # (1) 패키지.모듈.클래스()

print('ㅡㅡㅡㅡㅡㅡㅡ모듈 사용1ㅡㅡㅡㅡㅡㅡㅡ')
import math

print(math.pi)

print('ㅡㅡㅡㅡㅡㅡㅡ모듈 사용2ㅡㅡㅡㅡㅡㅡㅡ')
import math

print(math.sqrt(4.0))
print(math.sqrt(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈 사용 + 별명 지정ㅡㅡㅡㅡㅡㅡㅡ')
import math as m

print(m.sqrt(4.0))
print(m.sqrt(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 변수 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from math import pi

print(pi)

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 함수 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from math import sqrt

print(sqrt(4.0))
print(sqrt(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 함수 불러오기 + 별명 지정ㅡㅡㅡㅡㅡㅡㅡ')
from math import sqrt as s

print(s(4.0))
print(s(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 일부 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from math import pi, sqrt

print(pi)
print(sqrt(4.0))
print(sqrt(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 일부 불러오기 + 별명 지정ㅡㅡㅡㅡㅡㅡㅡ')
from math import pi as p, sqrt as s

print(p)
print(s(4.0))
print(s(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ모듈에서 모두 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from math import *

print(pi)
print(sqrt(4.0))
print(sqrt(2.0))

print('ㅡㅡㅡㅡㅡㅡㅡ패키지 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
import urllib.request

response = urllib.request.urlopen('http://www.google.co.kr')
print(response.status)

print('ㅡㅡㅡㅡㅡㅡㅡ패키지 불러오기 + 별명 지정ㅡㅡㅡㅡㅡㅡㅡ')
import urllib.request as r

response = r.urlopen('http://www.google.co.kr')
print(response.status)

print('ㅡㅡㅡㅡㅡㅡㅡ패키지에서 일부 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from urllib.request import Request, urlopen

req = Request('http://www.google.co.kr')
response = urlopen(req)
print(response.status)

print('ㅡㅡㅡㅡㅡㅡㅡ패키지에서 일부 불러오기 + 별명 지정ㅡㅡㅡㅡㅡㅡㅡ')
from urllib.request import Request as r, urlopen as u

req = r('http://www.google.co.kr')
response = u(req)
print(response.status)

print('ㅡㅡㅡㅡㅡㅡㅡ패키지에서 모두 불러오기ㅡㅡㅡㅡㅡㅡㅡ')
from urllib.request import *

req = Request('http://www.google.co.kr')
response = urlopen(req)
print(response.status)

print('ㅡㅡㅡㅡㅡㅡㅡ연습문제ㅡㅡㅡㅡㅡㅡㅡ')
from math import ceil, floor

x = 1.5
print(ceil(x), floor(x))