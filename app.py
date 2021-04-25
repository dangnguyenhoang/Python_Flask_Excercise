from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import requests
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS students (regnum TEXT, Name_ TEXT, email TEXT, hometown TEXT, birth TEXT, score TEXT)')

app=Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb@'
Bootstrap(app)

OPEN_WEATHER_API_KEY= 'd6230d83d36a641f42b755ee87c62fe6'
OPEN_WEATHER_URL = ('api.openweathermap.org/data/2.5/weather?zip={},uk&APPID=77d0e90e60b4eee00d6a9edf8997dd59')
@app.route('/')

# @app.route('/user/<name>')
# def user(name):
#     personal = f'<h1> Hello {name}, how are you</h1>'
#     return personal
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)