from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('test.db')
    return "App Connected to DB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
