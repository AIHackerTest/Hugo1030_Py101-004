# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request
from weather import fetch_weather

app = Flask(__name__)
history_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request' )
def process_request():
    city = request.args.get('city')
    try: # 调用weather.py中的fetch_weather函数，取得该城市天气值。
        weather_str = fetch_weather(city)
        history_list.append(weather_str)
        return render_template('query.html', weather_str=weather_str)
    except KeyError:
        if request.args.get('history') == "历史":
            return render_template("history.html", history_list=history_list)

        elif request.args.get('help') == "帮助":
            return render_template('help.html')

        else:
            return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True) # 启动调试模式，不必重启服务器。
