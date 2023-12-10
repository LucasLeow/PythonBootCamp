from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

blog_data = requests.get(
    url='https://api.npoint.io/c97283d17102d10ad110'
).json()
post_date = datetime.datetime.today()
@app.route('/')
def home():
    return render_template('index.html', posts=blog_data, date=post_date)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:blog_id>')
def post(blog_id):
    for blog in blog_data:
        if blog['id'] == blog_id:
            return render_template('post.html', post=blog, date=post_date)

if __name__ == '__main__':
    app.run(debug=True)