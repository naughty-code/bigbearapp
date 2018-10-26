from flask import Flask
import psycopg2
from flask_cors import CORS
from flask import jsonify
import os

DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__, static_url_path='')
CORS(app)

connection = psycopg2.connect(DATABASE_URL, sslmode='require')
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