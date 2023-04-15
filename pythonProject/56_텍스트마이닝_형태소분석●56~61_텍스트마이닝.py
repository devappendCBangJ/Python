# google >> jdk 검색 >> Oracle JAVE SE JDK 다운로드 >> 내 pc 오른쪽 마우스 클릭 >> 속성 >> 고급 시스템 설정 >> 환경 변수 클릭
# >> 시스템 변수 새로 만들기 >> JAVE SE JDK 폴더 지정 >> 확인 >> Pycharm 재실행
# >> https://velog.io/@junyoung9696/Konlpy-%EC%98%A4%EB%A5%98%EC%8B%9C-%EC%B0%B8%EA%B3%A0

# pip install jpype1
# pip install konlpy

# <형태소 분석기 종류>
# - 분석기의 종류에 따라 속도와 성능이 다름
    # konlpy Hannanum
    # konlpy Kkma
    # konlpy Komoran
    # konlpy Mecab
    # konlpy Okt
# - 문장에 따라 분석기의 결과가 달라짐
# - 다른 분석기를 쓰고 싶다면 구글링 해서 공부
# - konlpy 사이트에서 예제 확인 가능

# <형태소 분석>
# 0. 형태소 분석 모듈 불러오기 : import konlpy
# 0. 형태소 분석 모듈 불러오기 : from konlpy.tag import Okt
# 1. 형태소 분석 후 리스트형 안에 튜플형으로 저장 : Okt.pos("형태소 분석할 문장 or 문자")

from konlpy.tag import Okt

okt = Okt()
result = okt.pos("안녕하세요. 지금은 파이썬 공부 중입니다.")
print(result)