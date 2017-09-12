import sqlite3 as lite
import requests
import csv
import time

def fetch_weather(location):
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
    day = daily['date']
    text_day = daily['text_day']
    text_night = daily['text_night']
    high = daily['high']
    low = daily['low']
    wind_direction = daily['wind_direction']
    wind_scale = daily['wind_scale']
    return day, location, text_day, text_night, high, low, wind_direction, wind_scale

def create_database():
    con = lite.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Weathers")
        cur.execute("CREATE TABLE Weathers(\
                    Day TEXT, Location TEXT, Text_day TEXT, \
                    Texy_night TEXT, High TEXT, Low TEXT, \
                    wind_direction TEXT, wind_scale TEXT)")
    print("数据库已创建！")

def insert_database(day, location, text_day, text_night,
                    high, low, wind_direction, wind_scale):
    con = lite.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO Weathers VALUES (\
                    ?,?,?,?,?,?,?,?)',(
                    day, location, text_day, text_night,
                    high, low, wind_direction, wind_scale))

def get_cityweather():
    with open('cityname.csv', 'rt') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            for location in row:
                day, location, text_day, text_night, high, low, wind_direction, wind_scale = fetch_weather(location)
                insert_database(day, location, text_day, text_night, high, low, wind_direction, wind_scale)
                # time.sleep(21600)

def retrieve_data(city):
    con = lite.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT Day, Location, Text_day, Texy_night, High, Low, wind_direction, wind_scale FROM Weathers WHERE Location=:location",
            {'location': city})
        row = cur.fetchone()
        weather_str = u'{}，{}白天{}，夜晚{}。最高气温{}度，最低气温{}度。{}风{}级。'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return weather_str

def get_history():
    con = lite.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Weathers")
        rows = cur.fetchall()
    return rows

def update(location, weather):
    con = lite.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE Weathers SET Text_day=? WHERE Location=?", (weather, location))

if __name__=='__main__':
    create_database()
    get_cityweather()
