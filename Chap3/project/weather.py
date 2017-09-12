# -*- coding: utf-8 -*-
import requests

def fetch_weather(location):  # 用requests库，与API交互并获取信息
    result = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={
            'key': 'aavbujnax07w0irk',
            'location': location,
            'language': 'zh-Hans',
            'unit': ''
        },
        timeout=30)
    result = result.json()
    daily = result['results'][0]['daily'][1]
    date = daily['date']
    text_day = daily['text_day']
    text_night = daily['text_night']
    high = daily['high']
    low = daily['low']
    wind_direction = daily['wind_direction']
    wind_scale = daily['wind_scale']
    weather_str = u'{},{}白天{}，夜晚{}。最高气温{}度,最低气温{}度。{}风{}级。'.format(date, location, text_day, text_night, high, low, wind_direction, wind_scale)
    return weather_str
