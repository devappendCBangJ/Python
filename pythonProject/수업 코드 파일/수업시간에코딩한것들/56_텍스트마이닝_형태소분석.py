from konlpy.tag import Okt

okt = Okt()
result = okt.pos("안녕하세요. 지금은 파이썬 공부 중입니다.")
print(result)