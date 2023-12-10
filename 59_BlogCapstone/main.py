from flask import Flask, render_template, request
import requests
import datetime
import os
import smtplib

my_email = os.environ['my_email']
email_pw = os.environ['email_pw']
to_address = os.environ['to_address']

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form_data = None
    if request.method == 'POST':
        form_data = {}
        form_data['name'] = request.form['name']
        form_data['email'] = request.form['email']
        form_data['phone'] = request.form['phone']
        form_data['text_msg'] = request.form['text_msg']

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=f"Subject: New Message \n\n Name: {form_data['name']} \n Email: {form_data['email']} \n Phone: {form_data['phone']} \n Message: {form_data['text_msg']}"
            )
            print('Alert Mail Sent Successfully!')
        return render_template('contact.html', form_data=form_data)

    return render_template('contact.html')

@app.route('/post/<int:blog_id>')
def post(blog_id):
    for blog in blog_data:
        if blog['id'] == blog_id:
            return render_template('post.html', post=blog, date=post_date)


if __name__ == '__main__':
    app.run(debug=True)