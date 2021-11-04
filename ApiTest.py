import requests
#import sqlalchemy as db
import pandas as pd

url = "http://openapi.seoul.go.kr:8088/41694f6b566162633832477a616341/json/RealtimeCityAir/1/5"
response = requests.get(url)
parseResponse = response.json()

# print(parseResponse)

row = parseResponse["RealtimeCityAir"]["row"]

weather = []
# print(row)

for api in row:
    list = {}
    list["MSRDT"] = api["MSRDT"]
    list["MSRSTE_NM"] = api["MSRSTE_NM"]
    list["PM10"] = api["PM10"]
    list["IDEX_NM"] = api["IDEX_NM"]
    weather.append(list)

# print(weather)

weather_dataFrame = pd.DataFrame(weather)
print(weather_dataFrame)
