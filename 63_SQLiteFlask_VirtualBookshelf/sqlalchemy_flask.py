from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy()
db.init_app(app)


# Define model of Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create Table based on model
# need app context to execute command as though app running
with app.app_context(): # else, can run flaskapp, then run command in terminal
    db.create_all()

# Create
# with app.app_context():
#     first_book = Book(
#         title = 'Harry Potter 4',
#         author = 'J.K. Rowling',
#         rating = '9.3'
#     )
#
#     db.session.add(first_book)
#     db.session.commit()

#
# Read all
# with app.app_context():
#     result = db.session.execute(
#         db.select(Book).order_by(Book.title)
#     )
#     all_books = result.scalars() # get individual row from Result obj
#     print(all_books.first().id)

# Read all, alternate syntax
with app.app_context():
    result = db.session.execute(
        db.select(Book)
    ).scalar()
    print(result.id)
# # Read single
# with app.app_context():
#     book = db.session.execute(
#         db.select(Book).where(Book.id == 1)
#     ).scalar()
#
# # Update record by query
# with app.app_context():
#     book_to_update = db.session.execute(
#         db.select(Book).where(Book.title == 'Harry Potter')
#     ).scalar()
#     book_to_update.title = 'Harry Potter and Philosopher Stone'
#     db.session.commit()
#
# # Update by Primary Key
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(
#         db.select(Book).where(Book.id == book_id)
#     ).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# # Delete
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(
#         db.select(Book).where(Book.id == book_id)
#     ).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
