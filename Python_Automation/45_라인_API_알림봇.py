# line notify api 사이트 >> 가입 >> my page에서 key 발급 >> line notify api document 예제보면서 사용

# <post방식으로 정보 요청>
# requests.post("웹 사이트 주소", headers={'Request method' : '허가'}, data={'Parameter name' : '데이터'}
# - headers와 data는 딕셔너리 형태로 요청

import requests

# 1대1 알림
# api_key = "hUSpQNeP8igUtPZdcM1XaZBhDGnXJzKX8eF1QFx1FZM" # 내가 1대1 알림에 할당한 api
# h = {"Authorization" : "Bearer {}".format(api_key)}
# d = {"message" : "테스트 중입니다!!"}
# requests.post("https://notify-api.line.me/api/notify", headers=h, data=d)

# 단톡방 알림
api_key = "QAIxdX2oPirksnErNLO33QYQHPIUkyFUHghtk7N9nIn" # 내가 단톡방에 할당한 api
h = {"Authorization" : "Bearer {}".format(api_key)}
d = {"message" : "테스트 중입니다!!"}
requests.post("https://notify-api.line.me/api/notify", headers=h, data=d)