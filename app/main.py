from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='example',
        database='mydatabase'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NOW()')
    result = cursor.fetchone()
    conn.close()
    return f"Current time from MySQL: {result[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
