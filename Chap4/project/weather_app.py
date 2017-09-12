from flask import Flask, url_for, render_template, request
from database import fetch_weather, get_history, update, retrieve_data
import sqlite3 as lite

app = Flask(__name__)
history_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request' )
def process_request():
    city = request.args.get('city')
    if request.args.get('query') == "查询":
        weather_str = retrieve_data(city)
        history_list.append(weather_str)
        return render_template('query.html', weather_str=weather_str)
    elif request.args.get('history') == "历史":
        # history = get_history()
        return render_template("history.html", history_list=history_list)
    elif request.args.get('help') == "帮助":
        return render_template('help.html')
    elif request.args.get('update') == "更新":
        try:
            location, weather = city.split(" ")
            update(location, weather)
            return render_template('update.html')
        except ValueError:
            return render_template('updataerror.html')
    else:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
