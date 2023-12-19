from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os

SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

ckeditor = CKEditor(app)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class BlogForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])

    submit = SubmitField('SUBMIT POST')

# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    posts = db.session.execute(
        db.select(BlogPost)
    ).scalars().all()

    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/blog/<int:blog_id>')
def show_post(blog_id):
    blog = db.get_or_404(BlogPost, blog_id)
    if blog:
        return render_template('post.html', post=blog)
    else:
        return jsonify(
            response={
                "not found": "Sorry, a blog with that id was not found in the database"
            }
        ), 404


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def create_new_blog():
    form = BlogForm()
    if request.method == 'POST': # Create Form Submit
        if form.validate_on_submit(): # Create Form validated
            new_blog = BlogPost(
                title = form.title.data,
                subtitle = form.subtitle.data,
                date = date.today().strftime('%B %d, %Y'),
                body = form.body.data,
                author = form.author.data,
                img_url = form.img_url.data
            )
            db.session.add(new_blog)
            db.session.commit()

            return redirect(url_for('home'))
        else:
            return jsonify(
                response={
                    "form not validated": "Form not validated"
                }
            ), 400

    else: # GET form webpage
        return render_template('make-post.html', form=form, new_post=True)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    blog = db.get_or_404(BlogPost, post_id)
    if blog:
        form = BlogForm(obj=blog)
        if request.method == 'POST': # edit form submitted
            if form.validate_on_submit(): # edit form validated
                blog.title = form.title.data
                blog.subtitle = form.subtitle.data
                blog.body = form.body.data
                blog.author = form.author.data
                blog.img_url = form.img_url.data

                db.session.commit()
                return redirect(url_for('show_post', blog_id=blog.id))

            else:
                return jsonify(
                    response={
                        "form not validated": "Form not validated"
                    }
                ), 400
        else: # GET edit form
            return render_template("make-post.html", form=form, new_post=None)
    else: # blog not found
        return jsonify(
            response={
                "not found": "the blog with the given id was not found"
            }
        ), 404

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
