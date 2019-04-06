#!/usr/bin/env python
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/pinreader', methods=['POST'])
def pinreader():
    table_name = request.form['channel']
    time = request.form['time']
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()
        c.execute("insert into %s(time) values (?)" % table_name , (time,))
    return table_name

@app.route('/ui', methods=['GET'])
def ui():
    lasttime=0
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()
        c.execute("select * from start")
        starts = c.fetchall()
        c.execute("select * from meta")
        stops = c.fetchall()
    ind = min([len(starts), len(stops)])-1
    return str(stops[ind][1]-starts[ind][1])
