import sqlite3

db = sqlite3.connect('books-collection.db')

cur = db.cursor()

cur.execute(
    """
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title varchar(250) NOT NULL UNIQUE,
        author varchar(250) NOT NULL,
        rating FLOAT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')
    """
)

db.commit()