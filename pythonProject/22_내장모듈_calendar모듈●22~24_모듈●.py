# <내장모듈> 파이썬 내장 모듈
# 모듈 불러오기 : import 모듈명
# 모듈 불러오면서 별멍 지정 : import 모듈명 as 별명
# 모듈에서 함수만 불러오기 : from 모듈 import 함수
# 모듈 사용 : 모듈명.함수() or 별명.함수()
#파이썬 파일명과 특정 모듈명이 중복되면 안된다

from calendar import prmonth #from 모듈 import 함수 : 모듈에서 특정 함수만 불러옴(메모리 절약 / 사용 시 모듈명 안 써줘도 됨)
prmonth(2020, 11)