import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect,abort
# form submissions 
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

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

@app.route('/create', methods=('GET', 'POST'))
def create():
    # if the user clicked on Submit, it sends post request
    if request.method == 'POST':
        # Get the title and save it in a variable
        title = request.form['title']
        # Get the content the user wrote and save it in a variable
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            # Open a connection to databse
            conn = get_db_connection()
            # Insert the new values in the db
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                        (title, content))
            conn.commit()
            conn.close()
            # Redirect the user to index page
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:post_id>')
def post(post_id):
    # we got the post the user clicked on through the function we wrote before,
    # we save the value of the post in post variable
    post = get_post(post_id)
    # we render the post page, pass the post variable as an argument,
    #why? to be able to use it in the html page
    return render_template('post.html', post=post)
    
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    # Get the post to be edited by it's id
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            # Update the table 
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

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