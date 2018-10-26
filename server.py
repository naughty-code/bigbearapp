from flask import Flask
import psycopg2
from flask_cors import CORS
from flask import jsonify
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path='')
CORS(app)

connection = psycopg2.connect(dbname='d4pp6fmbq2237a', user='hseahwenpwiswg', password='2e56524af38f5e01ed406d57e3631d05782128a2239fca9ca7ebeb05014cb638', host='ec2-184-73-169-151.compute-1.amazonaws.com', port='5432')
cursor = connection.cursor()

@app.route('/api/cabins')
def cabins():
    cursor.execute('SELECT * FROM db.cabin')
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/api/vrm')
def vrm():
    cursor.execute('SELECT * FROM db.vrm')
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/')
def root():
    return app.send_static_file('index.html')

cursor.close()
connection.close()