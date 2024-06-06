import sqlite3
from flask import Flask, render_template, abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # allows us to access columns by name instead of index
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    # we got the post the user clicked on through the function we wrote before,
    # we save the value of the post in post variable
    post = get_post(post_id)
    # we render the post page, pass the post variable as an argument,
    #why? to be able to use it in the html page
    return render_template('post.html', post=post)
    

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
   app.run()