#!/usr/bin/env python3
#-*-coding:utf-8 -*-
'''
利用「心知天气」API，查询天气。
输入城市名，查询该城市的天气；
输入 help, 获取帮助文档；
输入 history, 获取查询历史；
输入 c，切换到摄氏度；
输入 f，切换到华氏度；
输入 0，查询今天天气；
输入 1，查询明天天气；
输入 2，查询后天天气；
输入 quit, 退出天气查询系统。
'''
__version__ = "V17.8.20.1902"
__author__ = "hugo"
__lisence__ = "MIT@2017-08"

import requests

history_list = []
unit = 'c'
i = 0

def fetch_weather(location, unit):  # 用requests库，与API交互并获取信息
    result = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={
            'key': 'aavbujnax07w0irk',
            'location': location,
            'language': 'zh-Hans',
            'unit': unit
        },
        timeout=20)
    return result.json()

def show_weather(result, i):  # 处理JSON格式信息
    daily = result['results'][0]['daily'][i]
    date = daily['date']
    text_day, text_night = daily['text_day'], daily['text_night']
    high, low = daily['high'], daily['low']
    wind_direction, wind_scale = daily['wind_direction'], daily['wind_scale']
    weather_str = f'{date}\n{order}白天{text_day},夜晚{text_night}。\
        \n最高气温{high}度,最低气温{low}度\n{wind_direction}风{wind_scale}级。\n'
    return weather_str

while True:
    order = input('请输入指令或您要查询的城市名：')
    try:  # 显示查询信息，并保存到history列表中
        result = fetch_weather(order, unit)
        weather_str = show_weather(result, i)
        print(weather_str)
        history_list.append(weather_str)

    except KeyError:
        if order in ['h', 'help']:
            print('''
                输入城市名，查询该城市的天气；
                输入 help, 获取帮助文档；
                输入 history, 获取查询历史；
                输入 c，切换到摄氏度；
                输入 f，切换到华氏度。
                输入 0，查询今天天气；
                输入 1，查询明天天气；
                输入 2，查询后天天气。
                输入 quit, 退出天气查询系统。
            ''')

        # 温度切换
        elif order in ['c', 'f']:
            unit = order
            print('已切换温度\n')

        # 指定查询今天、明天或后天的天气
        elif order in ['0', '1' ,'2']:
            i = int(order)
            print('已切换查询日期\n')

        # 查询历史记录
        elif order in ['history']:
            for info in history_list:
                print(info)

        # 返回历史记录，退出程序
        elif order in ['quit', 'q']:
            print("退出查询系统！")
            break

        else:
            print('没有该城市信息!请输入help查看帮助文档。')
