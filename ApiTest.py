from os import replace
import requests
import sqlalchemy as db
import pandas as pd

# 1. http 통신을 위해 requests 모듈로 데이터 다운 받기
url = "http://openapi.seoul.go.kr:8088/41694f6b566162633832477a616341/json/RealtimeCityAir/1/5"
response = requests.get(url)
parseResponse = response.json()

# print(parseResponse)

# 2. 파이썬 list로 데이터 정제하기
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

# 3. Pandas로 데이터 변경하기
weather_dataFrame = pd.DataFrame(weather)
print(weather_dataFrame)

# 4. DB연결 하기

engine = db.create_engine(
    "mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")
