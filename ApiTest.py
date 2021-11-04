import requests
#import sqlalchemy as db
#import pandas as pd

url = "http://openapi.seoul.go.kr:8088/41694f6b566162633832477a616341/json/RealtimeCityAir/1/5"
response = requests.get(url)
parseResponse = response.json()

print(parseResponse)
