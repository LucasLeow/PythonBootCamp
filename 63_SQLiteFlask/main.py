from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"

db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    all_books = db.session.execute(
        db.select(Book)
    )
    return render_template('index.html', books=all_books) # books is ChunkedIteratorObject


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        new_book = Book(
            title = request.form['name'],
            author = request.form['author'],
            rating = request.form['rating']
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):

    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()

    if request.method == 'POST':
        new_rating = request.form['rating']
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit_rating.html', book=book_to_update)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

