import json
import requests

api_key = "108dbe8bc77f920712ee49138e0fe752"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul", api_key)
data = requests.get(url)
result = json.loads(data.text)  # json -> 딕셔너리 자료형으로 변환
print(result["name"])
print(result["weather"][0]["main"])
