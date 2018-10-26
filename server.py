from flask import Flask
import psycopg2
from flask_cors import CORS
from flask import jsonify
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/api/cabins')
def api():
    connection = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM db.cabin')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

@app.route('/api/vrm')
def vrm():
    connection = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM db.vrm')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

@app.route('/')
def root():
    return app.send_static_file('index.html')

