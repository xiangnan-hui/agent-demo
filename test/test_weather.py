import requests

API_KEY = "4efea704813f215497d8f2e980cda761"

url = "https://restapi.amap.com/v3/weather/weatherInfo"

params = {
    "key": API_KEY,
    "city": "110000",   # 北京
    "extensions": "base"
}

res = requests.get(url, params=params)

print(res.status_code)
print(res.json())