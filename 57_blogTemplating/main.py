from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
post_objs = []

@app.route('/')
def home():
    blog_posts = requests.get(
        url='https://api.npoint.io/faf15a28b24b43cc6682'
    ).json()

    for post in blog_posts:
        post_objs.append(Post(post['id'], post['title'], post['subtitle'], post['body']))

    return render_template("index.html", posts=post_objs)


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    desired_post = None
    for post in post_objs:
        if post.id == blog_id:
            desired_post = post
    return render_template('post.html', post=desired_post)

if __name__ == "__main__":
    app.run(debug=True)
