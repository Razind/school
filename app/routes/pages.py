from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Page, Heading, TextBlock, Link, Media, Section, Element
from ..extensions import db
from ..forms import PageForm, EditPageForm


page_bp = Blueprint('pages_bp', __name__)

# View all pages
@page_bp.route('/all', methods=['GET', 'POST'])
def pages_all():
    pages = Page.query.all()  # Получаем все страницы из базы данных
    return render_template('pages_all.html', pages=pages)  # Передаем страницы в шаблон

@page_bp.route('/page_preview/<int:page_id>')
def page_preview(page_id):
    page = Page.query.get_or_404(page_id)
    sections = Section.query.filter_by(page_id=page.id).order_by(Section.order).all()

    for section in sections:
        section.elements = Element.query.filter_by(section_id=section.id).order_by(Element.order).all()

    return render_template('preview_page.html', page=page, sections=sections)

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

@page_bp.route('/page/<slug>')
def view_page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()

    # Получаем секции и сортируем их по полю `order`
    sections = Section.query.filter_by(page_id=page.id).order_by(Section.order).all()

    # Для каждой секции получаем элементы, отсортированные по полю `order`
    for section in sections:
        section.elements = Element.query.filter_by(section_id=section.id).order_by(Element.order).all()

    return render_template('view_page.html', page=page, sections=sections)

