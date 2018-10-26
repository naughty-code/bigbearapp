from flask import Flask
import psycopg2
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/api')
def api():
    connection = psycopg2.connect(dbname='d4pp6fmbq2237a', user='hseahwenpwiswg', password='2e56524af38f5e01ed406d57e3631d05782128a2239fca9ca7ebeb05014cb638', host='ec2-184-73-169-151.compute-1.amazonaws.com', port='5432')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM db.cabin')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

@app.route('/')
def root():
    return app.send_static_file('index.html')