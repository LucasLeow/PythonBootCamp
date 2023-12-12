### Flask WTForm Summary
---
#### Modules Required
Bootstrap_Flask\==2.2.0
Flask\==2.3.2
Flask_WTF\==1.1.1
WTForms\==3.0.1

#### Method 1: Manual Creation of Form
Steps:
1. import all necessary library
```
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
# pip install email_validator (for Email validator)
```
2. create form class in python
```
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
```
3. pass form as dependency to form html  eg: 
```
return render_template('login.html', form=login_form)
```
4. create form html with jinja templating to access fields
```
			<form method="POST" action="{{ url_for('login') }}" novalidate>
				{{ form.csrf_token }}
				<p>
					{{ form.email.label }} {{ form.email(size=30) }}
					{% for err in form.email.errors %}
					<span style="color: red;"> {{ err }}</span>
					{% endfor %}
				</p>
				<p>
					{{ form.password.label }} {{form.password(size=30) }}
					{% for err in form.password.errors %}
					<span style="color: red;"> {{ err }}</span>
					{% endfor %}
				</p>
					{{ form.submit }}
			</form>
```
> Side note:
> - novalidate to disable default browser form validation (to use WTform validation instead)

### Accessing form data upon submit 
- login_form.email.data
- login_form.password.data
```
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():  # To trigger validators for formfields (return True / False)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == 'admin':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # need to include novalidate in <form novalidate> to disable default html form validation
    return render_template('login.html', form=login_form)

```


### Jinja Templating Inheritance
> {% block <desired_name>}
\<content> <- in child classes, in parent class, no content
{% endblock %}

eg:
1. Create base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %} {% endblock %} </title>
    {% block styling %}
        {{ bootstrap.load_css() }}
    {% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
2. index, success and denied html inherits from base
success.html:
```
{% extends 'base.html' %}
{% block title %} Success {% endblock %}
{% block content %}
	<div class="container">
		<h1>Success</h1>
	</div>
{% endblock %}
```

denied.html: (super() to modify some of superclass inheritance)
```
{% extends 'base.html' %}
{% block title %} Denied {% endblock %}
{% block styling %}
	{{ super() }}
	h1 {
		color: red;
	}
{% endblock %}
{% block content %}
	<div class="container">
		<h1>Denied</h1>
	</div>
{% endblock %}
```

index.html:
```
{% extends 'base.html' %}
{% block title %} Secrets {% endblock %}
{% block content %}
    <div class="jumbotron">
      <div class="container">
        <h1>Welcome</h1>
        <p>Are you ready to discover my secret?</p>
        <a class="btn btn-primary btn-lg" href=" {{ url_for('login') }} "
          >Login</a
        >
      </div>
    </div>
{% endblock %}
```

### Bootstrap-Flask implementation
```
from flask_bootstrap import Bootstrap5
```

```
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

bootstrap = Bootstrap5(app)
```

Inside base.html:
```
    <title>{% block title %} {% endblock %} </title>
    {{ bootstrap.load_css() }}
```
> Then can use bootstrap class convention as required, just need to render css using code above

### Bootstrap flask form implementation
1. go to form html
```
{% extends 'base.html' %}
{% from 'bootstrap5/form.html' import render_form %}
{% block title %} Login {% endblock %}
{% block content %}
        <div class="container">
			<h1>Login</h1>
			{{ render_form(form) }}
        </div>
{% endblock %}
```