from langchain.tools import tool
from service.weather_service import WeatherService
import random


@tool(description="获取指定城市天气（真实高德API）")
def get_weather(city: str) -> str:

    service = WeatherService()
    result = service.get_weather(city)

    # 高德返回结构处理
    if result.get("status") == "1":
        live = result["lives"][0]

        return (
            f"城市：{live['city']}\n"
            f"天气：{live['weather']}\n"
            f"温度：{live['temperature']}°C\n"
            f"湿度：{live['humidity']}%\n"
            f"风向：{live['winddirection']}\n"
            f"风力：{live['windpower']}"
        )

    return "天气获取失败"