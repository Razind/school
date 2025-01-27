from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Page, Heading, TextBlock, Link, Media
from ..extensions import db
from ..forms import PageForm, EditPageForm


page_bp = Blueprint('pages_bp', __name__)

# View all pages
@page_bp.route('/all', methods=['GET', 'POST'])
def pages_all():
    pages = Page.query.all()  # Получаем все страницы из базы данных
    return render_template('pages_all.html', pages=pages)  # Передаем страницы в шаблон

# Create a new page
@page_bp.route('/create', methods=['GET', 'POST'])
def create_page():
    form = PageForm()  # Создаем форму
    if request.method == 'POST' and form.validate_on_submit():
        # Обрабатываем данные формы
        name = form.name.data
        slug = form.slug.data
        page = Page(name=name, slug=slug)
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('pages_bp.pages_all'))  # Перенаправление на список страниц

    return render_template('create_page.html', form=form)  # Передаем форму в шаблон

# Edit a page
@page_bp.route('/edit/<int:page_id>', methods=['GET', 'POST'])
def edit_page(page_id):
    page = Page.query.get_or_404(page_id)  # Используем page_id
    form = EditPageForm(obj=page)  # Инициализация формы с данными страницы
    
    if form.validate_on_submit():  # Проверка на отправку формы
        page.name = request.form['name']  # Обновляем поле name
        page.slug = request.form['slug']  # Обновляем поле slug
        db.session.commit()  # Сохраняем изменения
        return redirect(url_for('pages_bp.pages_all'))  # Перенаправление после успешного сохранения

    return render_template('edit_page.html', page=page, form=form)

# Add text block to page
@page_bp.route('/pages/<int:page_id>/add_text', methods=['GET', 'POST'])
def add_text(page_id):
    page = Page.query.get(page_id)
    if request.method == 'POST':
        text = request.form['text']
        text_block = TextBlock(content=text, page_id=page.id)
        db.session.add(text_block)
        db.session.commit()
        return redirect(url_for('page.edit_page', id=page.id))

    return render_template('add_text.html', page=page)

# View a page by its slug
@page_bp.route('/page/<slug>')
def view_page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()
    headings = Heading.query.filter_by(page_id=page.id).all()
    text_blocks = TextBlock.query.filter_by(page_id=page.id).all()
    links = Link.query.filter_by(page_id=page.id).all()
    media = Media.query.filter_by(page_id=page.id).all()

    return render_template('view_page.html', page=page, headings=headings, text_blocks=text_blocks, links=links, media=media)
