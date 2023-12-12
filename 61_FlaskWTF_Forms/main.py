from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
# pip install email_validator (for Email validator)
import os

from flask_bootstrap import Bootstrap5


secret_key = os.environ['secret_key']

class LoginForm(FlaskForm):
    # validators accept list of validator objects, eg DataRequired makes field Required
    email = StringField('email', validators=[
        DataRequired(),
        Email(message=('Not a valid email address'))
    ])
    password = PasswordField('password', validators=[
        DataRequired(),
        Length(min=8, message=('minimum 8 characters for password'))
    ])
    submit = SubmitField(label='Log In')
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit(): # To trigger validators for formfields (return True / False)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == 'admin':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # need to include novalidate in <form novalidate> to disable default html form validation
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
