## 1 User Registration
* getting info. from form
* flash msg if user registered
* hash + salt password
```
from flask import Flask, jsonify, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
```
```
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
```

## 2 Managing User Sessions
* After user login
* using flask-login module
```
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
```
### Login
```
SECRET_KEY = os.environ['SECRET_KEY']  # required by Flask-Login
app.config['SECRET_KEY'] = SECRET_KEY

# CONFIGURE FLASK LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model): # UserMixin for multiple inheritance (is_active)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
    
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
        return render_template("login.html")
```
### Logout
```
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
```
### Requiring User Auth
```
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)  # current_user is keyword used by flask-login
    

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')
```

### Flashing message
```
from flask import flash
```
```
def register():
    if request.method == 'POST':  # Register form submit
        email = request.form.get('email')
        user = db.session.execute(
            db.select(User).where(User.email == email)
        )
        if user:
            flash('Email already registered. Login instead')
            return redirect(url_for('login'))
        .
        .
        .
```
### login.html
```
{% with message = get_flashed_messages()[0] %}
  <div class="box">
    <h1>Login</h1>
    <!-- TODO: Use Message Flashing to display feedback to the user with a <p> -->
    {% if message %}
    <p> {{ message }}</p>
    {% endif %}

    <form action="{{ url_for('login') }}" method="post">
    .
    .
    </form>
  </div>
{% endwith %}
```
### Render view based on authentication status
* user logged in 
* user logged out
### Base.html
```
    {% if not logged_in: %}
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('login') }}">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('register') }}">Register</a>
          </li>
    {% endif %}
```
### index.html
```
  {% if not logged_in %}
  
      <a href="{{ url_for('login') }}" class="btn btn-primary btn-block btn-large"
        >Login</a
      >
      <a
        href="{{ url_for('register') }}"
        class="btn btn-secondary btn-block btn-large"
        >Register</a
      >
      
  {% else %}
  
    <p> (You are already logged in) </p>

  {% endif %}
```
```
return render_template("register.html", logged_in=current_user.is_authenticated)

return render_template("login.html", logged_in=current_user.is_authenticated)

return render_template("secrets.html", name=current_user.name, logged_in=True) 
```