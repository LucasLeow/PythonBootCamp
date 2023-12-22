from flask import Flask, jsonify, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

SECRET_KEY = os.environ['SECRET_KEY']  # required by Flask-Login
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# CONFIGURE FLASK LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # Register form submit
        email = request.form.get('email')
        user = db.session.execute(
            db.select(User).where(User.email == email)
        )
        if user:
            flash('Email already registered. Login instead')
            return redirect(url_for('login'))

        user_password = request.form.get('password')
        hash_password = generate_password_hash(
            password=user_password,
            method='pbkdf2',
            salt_length=8
        )
        new_user = User(
            email=email,
            name=request.form.get('name'),
            password=hash_password
        )

        db.session.add(new_user)
        db.session.commit()

        # Login user after registration & adding details to db
        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Get user
        user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        if not user:  # user not exist (None)
            flash('That email does not exist. Please try again')
            return redirect(url_for('login'))

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Incorrect password. Please try again')
            return redirect(url_for('login'))

    else:  # GET Login page
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)  # current_user is keyword used by flask-login


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
