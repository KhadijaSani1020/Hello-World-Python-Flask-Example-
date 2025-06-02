from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Render!"

@app.route('/create')
def create_table():
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name TEXT);")
        conn.commit()
        cur.close()
        conn.close()
        return "Table created successfully!"
    except Exception as e:
        return f"Error: {e}"
