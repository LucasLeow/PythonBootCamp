## Step 1: Create Form Class

```
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
```

```
class BlogForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[])
    content = CKEditorField('Blog Content', validators=[])

    submit = SubmitField('SUBMIT POST')

```

## Step 2: Create form instance inside route fn
```
@app.route('/new-post', methods=['GET', 'POST'])
def create_new_blog():
    form = BlogForm()
    if request.method == 'POST': # Form Submit
        if form.validate_on_submit(): # Form validated
            print('Form validated')
            print(form.title.data)
        else:
            print('Form not validated')
    else: # GET form webpage
        return render_template('make-post.html', form=form)
```

## Step 3: Include link to form function
>index.html
```
        <a
          class="btn btn-primary float-right"
          href="{{ url_for('create_new_blog') }}"
          >Create New Post</a
        >
```

## Step 4: Edit Form HTML to render form
> make-post.html
```
{% block content %} {% include "header.html" %}
{% from 'bootstrap5/form.html' import render_form %}
<!-- Page Header -->
<header
  class="masthead"
  style="background-image: url('../static/assets/img/edit-bg.jpg')"
>
.
.
.

      <div class="col-lg-8 col-md-10 mx-auto">
        <!-- TODO:-Add CKEditor and render the form here -->
            {{ ckeditor.load() }}
            {{ ckeditor.config(name='content') }}
            {{ render_form(form) }}
      </div>
```