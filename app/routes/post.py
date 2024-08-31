from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_login import login_required
from datetime import datetime
from ..extensions import db
from ..models.post import Post
from ..models.question import Question
import os
from werkzeug.utils import secure_filename
from ..forms import NewsForm
from ..functions import save_image

post = Blueprint('post', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@post.route('/', methods=['POST', 'GET'])
def all():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    for post in posts:
        if isinstance(post.date_posted, str):
            post.date_posted = datetime.strptime(post.date_posted, '%Y-%m-%d %H:%M:%S')
    return render_template('main/index.html', posts=posts)

@post.route('/post/<int:id>', methods=['POST', 'GET'])
def view_post(id):
    post = Post.query.get_or_404(id)
    return render_template('main/post.html', post=post)

@post.route('/adminpost/<int:id>', methods=['POST', 'GET'])
@login_required
def view_postadmin(id):
    post = Post.query.get_or_404(id)
    num_questions = Question.query.count()  # Пример получения количества вопросов
    return render_template('admin/adminpost.html', post=post, num_questions=num_questions)

@post.route('/admin/news', methods=['POST', 'GET'])
@login_required
def admin_news():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    for post in posts:
        if isinstance(post.date_posted, str):
            post.date_posted = datetime.strptime(post.date_posted, '%Y-%m-%d %H:%M:%S')
    num_questions = Question.query.count()  # Пример получения количества вопросов
    return render_template('admin/news.html', posts=posts, num_questions=num_questions)

@post.route('/post/create', methods=['POST', 'GET'])
@login_required
def create():
    form = NewsForm()
    if form.validate_on_submit():
        image_filename = save_image(form.image.data)
        post = Post(title=form.title.data, content=form.content.data, image=image_filename)
        db.session.add(post)
        db.session.commit()
        flash('Новость успешно создана!', 'success') 
        print('ой ой ой кто то создал новость')
        return redirect('/admin/news')  # добавьте return перед redirect
    else:
        flash('Пожалуйста, исправьте ошибки в форме.', 'danger')
        print('Аларм!! Ошибочка произошла')
    num_questions = Question.query.count()  # Пример получения количества вопросов
    return render_template('admin/create.html', form=form, num_questions=num_questions)

@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
@login_required
def update(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')

        try:
            db.session.commit()
            return redirect(url_for('post.admin_news'))
        except Exception as e:
            print(str(e))
            return render_template('admin/update.html', post=post, error=str(e))
    else:
        num_questions = Question.query.count()  # Пример получения количества вопросов
        return render_template('admin/update.html', post=post, num_questions=num_questions)

@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
    post = Post.query.get(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('post.admin_news'))
    except Exception as e:
        print(str(e))
        return str(e)