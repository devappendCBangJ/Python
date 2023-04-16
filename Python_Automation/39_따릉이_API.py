# 파일의 절대경로 반환 : os.path.abspath("파일 위치 / 파일 이름")

import requests #url 불러오기
import json #json을 딕셔너리형으로 전환
import folium #지도
import os #파일 경로 관련 함수
from selenium import webdriver #웹 브라우저 동작

# api url에서 받은 코드 가공
api_key = "★sid_key★"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/100/".format(api_key)
data = requests.get(url)
print(data.text) #확인용 코드
result = json.loads(data.text)
# print(json.dumps(result, indent="\t")) #확인용 코드
rows = result["rentBikeStatus"]["row"]
print(rows)

# api에서 받는 정보 기반으로 지도 띄우기
lat_sum = 0
lon_sum = 0
for i in rows:
    latitude = i["stationLatitude"]
    longitude = i["stationLongitude"]
    lat_sum += float(latitude) #float() : 문자열 -> 실수형
    lon_sum += float(longitude)
lat_aver = lat_sum/len(rows)
lon_aver = lon_sum/len(rows)
map = folium.Map(location=[lat_aver, lon_aver], zoom_start=13.2)

# 지도에 마커 생성 후 저장
for i in rows:
    # print(i) #확인용 코드
    bike_num = int(i["parkingBikeTotCnt"])
    station_name = i["stationName"]
    latitude = i["stationLatitude"]
    longitude = i["stationLongitude"]
    if bike_num < 3:
        color = "red"
    elif 3 <= bike_num < 7:
        color = "blue"
    elif 7 < bike_num:
        color = "green"
    folium.Marker(location=[latitude, longitude], popup=station_name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map)
map.save("./map.html")

# 지도 불러오기
file_path = os.path.abspath("./map.html")
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(file_path)