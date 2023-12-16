from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

secret_key = os.environ['SECRET_KEY']
bearer_token = os.environ['BEARER']
moviedb_url = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"

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
    ranking = db.Column(db.Integer, unique=True)
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

class AddForm(FlaskForm):
    title = StringField(
        label='Movie Title',
        validators=[DataRequired()]
    )
    submit = SubmitField(label='Add Movie')


# Run this code to generate db instance (on first run)
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

@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    add_form = AddForm()
    if request.method == 'POST': # POST form (form submit)
        if add_form.validate_on_submit():
            movie_title = add_form.title.data

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {bearer_token}"
            }

            movie_params = {
                'query': movie_title,
                'include_adult': False,
                'language': 'en-US',
                'page': 1
            }

            response = requests.get(
                moviedb_url,
                headers=headers,
                params=movie_params
            )

            all_movies = response.json()['results']

            return render_template('select.html', movies=all_movies)
        else:
            print('add form not validated')

    else: # GET form
        return render_template('add.html', form=add_form)

@app.route('/<int:movie_id>')
def movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    movie_data = requests.get(url, headers=headers).json()
    new_movie = Movie(
        title = movie_data['original_title'],
        year = movie_data['release_date'][:4],
        description = movie_data['overview'],
        rating = movie_data['vote_average'],
        ranking = None,
        review = "",
        img_url = f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()

    desired_movie = db.session.execute(
        db.select(Movie).where(Movie.title == movie_data['original_title'])
    ).scalar()

    return redirect(url_for('edit_rating', movie_id=desired_movie.id))

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
            print('edit form not validated')

    else:  # GET form
        return render_template("edit.html", form=edit_form)

@app.route('/delete')
def delete_movie():
    movie_id = request.args.get('movie_id')
    movie_to_delete = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()

    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
