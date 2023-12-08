from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', random_num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    age_URL = 'https://api.agify.io/'
    gender_URL = 'https://api.genderize.io'

    params = {
        'name': name
    }

    age_res = requests.get(
        url=age_URL,
        params=params
    ).json()

    gender_res = requests.get(
        url=gender_URL,
        params=params
    ).json()

    age = age_res['age']
    gender = gender_res['gender']

    return render_template('index.html', name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = 'https://api.npoint.io/faf15a28b24b43cc6682'
    all_posts = requests.get(url=blog_url).json()
    return render_template('multiline_jinja.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)