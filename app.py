from flask import Flask, render_template

from helpfunctions import *

app = Flask(__name__)

@app.before_request
def before_first_reqest():
    init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def get_post(post_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES ("Random Title", "Lorem ipsum dolor sit amet consectetur adipiscing elit")')
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run()

