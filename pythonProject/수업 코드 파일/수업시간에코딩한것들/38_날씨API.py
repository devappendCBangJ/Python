import requests # 터미널 창에 pip install requests
import json

api_key = "bc496d10dc4e2b26e98c7235d4e2006f"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul", api_key)
data = requests.get(url)
result = json.loads(data.text) # json -> 딕셔너리 자료형으로 변환
print("도시 :", result["name"])
print("현재날씨 :", result["weather"][0]["main"])
print("최저기온 :", result["main"]["temp_min"])
print("최고기온 :", result["main"]["temp_max"])