import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # allows us to access columns by name instead of index
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('base.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route("/post")
def posts():
    return "<p>This is a post</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
   app.run()