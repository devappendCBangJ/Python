import requests
import json
import folium
import os
from selenium import webdriver

api_key = "57756a625673776a38324c4d447070"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/100/".format(api_key)
data = requests.get(url)
result = json.loads(data.text) # json -> 딕셔너리 자료형
# print(json.dumps(result, indent="\t"))
rows = result["rentBikeStatus"]["row"]
lat_sum = 0
lon_sum = 0
for i in rows:
    lat = float(i["stationLatitude"]) # float() : 문자열 -> 실수형
    lon = float(i["stationLongitude"])
    lat_sum += lat
    lon_sum += lon
lat_avr = lat_sum/len(rows)
lon_avr = lon_sum/len(rows)

map = folium.Map(location=[lat_avr, lon_avr], zoom_start=14)
for i in rows:
    bike_num = int(i["parkingBikeTotCnt"])
    station_name = i["stationName"]
    lat = i["stationLatitude"]
    lon = i["stationLongitude"]
    if bike_num < 3:
        color = "red"
    elif 3 <= bike_num < 7:
        color = "blue"
    elif 7 <= bike_num:
        color = "green"
    folium.Marker(location=[lat, lon], popup=station_name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map)
map.save("./map.html")

file_path = os.path.abspath("./map.html") # 파일의 절대 경로를 반환.
browser = webdriver.Chrome("./chromedriver")
# browser.get(file_path) # 윈도우 사용자
browser.get("file://" + file_path) # 맥 사용자