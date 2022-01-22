import requests
import json
import folium
import os
from selenium import webdriver

api_key = "425271794a6b696d3439727370716b"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/100/".format(api_key)
data = requests.get(url)
result = json.loads(data.text)  # json -> 딕셔너리
# print(json.dumps(result, indent="\t"))
bikes = result["rentBikeStatus"]["row"]
# 좌표 중심값 구하기
lat_sum = 0
lon_sum = 0
for i in bikes:
    lat_sum += float(i["stationLatitude"])
    lon_sum += float(i["stationLongitude"])
lat_avr = lat_sum / len(bikes)
lon_avr = lon_sum / len(bikes)

map = folium.Map([lat_avr, lon_avr], zoom_start=14)
for i in bikes:
    station_name = i["stationName"]
    bike_num = int(i["parkingBikeTotCnt"])  # 문자열 -> 정수형
    if bike_num < 3:
        color = "red"
    elif 3 <= bike_num < 7:
        color = "blue"
    else:
        color = "green"
    lat = float(i["stationLatitude"])  # 문자열 -> 실수형
    lon = float(i["stationLongitude"])
    folium.Marker([lat, lon], popup=station_name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map)
map.save("./따릉이.html")

path = os.path.abspath("./따릉이.html")
browser = webdriver.Chrome("./chromedriver")
browser.get(path)
# 창 유지
while (True):
    pass
