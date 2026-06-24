from utils.config_handler import weather_conf
import requests


class WeatherService:

    def __init__(self):
        self.api_key = weather_conf["AMAP_API_KEY"]

    def get_weather(self, city_code):

        url = "https://restapi.amap.com/v3/weather/weatherInfo"

        params = {
            "key": self.api_key,
            "city": city_code,
            "extensions": "base"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        return response.json()

if __name__ == '__main__':
    service = WeatherService()
    result = service.get_weather("110000")
    print(result)