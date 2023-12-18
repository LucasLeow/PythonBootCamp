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
    content = StringField('Blog Content', validators=[])

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
```
        <a
          class="btn btn-primary float-right"
          href="{{ url_for('create_new_blog') }}"
          >Create New Post</a
        >
```

## Step 4: Edit Form HTML to render form