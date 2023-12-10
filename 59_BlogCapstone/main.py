from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

blog_data = requests.get(
    url='https://api.npoint.io/c97283d17102d10ad110'
).json()

@app.route('/')
def home():
    return render_template('index.html', posts=blog_data, date=datetime.datetime.today())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)