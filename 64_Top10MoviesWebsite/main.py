from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
secret_key = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = secret_key
Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class RatingForm(FlaskForm):
    rating = StringField(
        label='Your rating out of 10. e.g. 7.5',
        validators=[DataRequired()]
    )
    review = StringField(
        label='Your Review',
        validators=[DataRequired()]
    )
    submit = SubmitField(label='Done')


# Create 1st instance for testing
# with app.app_context():
#     db.create_all()

# with app.app_context():
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.execute(
        db.select(Movie).order_by(Movie.ranking.desc())
    )
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit_rating(movie_id):
    edit_form = RatingForm()

    if request.method == 'POST':  # POST form (form submit)
        movie_to_update = db.session.execute(
            db.select(Movie).where(Movie.id == movie_id)
        ).scalar()

        if edit_form.validate_on_submit():  # trigger validators for formfield
            movie_to_update.rating = edit_form.rating.data
            movie_to_update.review = edit_form.review.data

            db.session.commit()
            return redirect(url_for('home'))

        else:
            print('not validated')

    else:  # GET form
        return render_template("edit.html", form=edit_form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
