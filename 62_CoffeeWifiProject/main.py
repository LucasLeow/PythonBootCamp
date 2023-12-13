from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
SECRET_KEY = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)

COFFEE_RATINGS = ['☕️' * i for i in range(1, 6)]
WIFI_RATINGS = ['✘'] + ['💪' * i for i in range(1, 6)]
SOCKET_RATINGS = ['🔌' * i for i in range(1, 6)]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(), URL(require_tld=True, message='invalid URL')])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=COFFEE_RATINGS, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=WIFI_RATINGS, validators=[DataRequired()])
    socket = SelectField('Power Socket Availability', choices=SOCKET_RATINGS, validators=[DataRequired()])

    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        fields = [
            form.cafe.data,
            form.cafe_location.data,
            form.open_time.data,
            form.close_time.data,
            form.rating.data,
            form.wifi_rating.data,
            form.socket.data
        ]
        print(fields)
        with open(r'cafe-data.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        print('cafe successfully appended')
        return redirect(url_for('add_cafe'))
    else:
        print('Form invalidated')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
