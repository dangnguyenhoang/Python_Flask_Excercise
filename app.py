from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import requests
import sqlite3 as sql

conn = sql.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS students (Regnum TEXT, Name_ TEXT, Email TEXT, Hometown TEXT, DoB TEXT, Score TEXT)')


app=Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb@'
Bootstrap(app)


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         Regnum= request.form['Regnum']
         Name_ = request.form['Name_']
         Email = request.form['Email']
         Hometown = request.form['Hometown']
         DoB = request.form['DoB']
         Score = request.form['Score']
         
         with sql.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO students (Regnum,Name_,Email,Hometown,DoB,Score) VALUES (?,?,?,?,?,?)",(Regnum,Name_,Email,Hometown,DoB,Score) )
            
            conn.commit()
            msg = "Record successfully added"
      except:
         conn.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("index.html")
         conn.close()

@app.route('/list')
def list():
   conn = sql.connect("database.db")
   conn.row_factory = sql.Row
   
   cur = conn.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("List.html",rows = rows)
   conn.close()

if __name__ == '__main__':
    app.run(debug=True)