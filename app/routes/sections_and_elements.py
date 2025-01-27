from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Page, Section, Element
from ..extensions import db
from ..forms import SectionForm, ElementForm

section_bp = Blueprint('section_bp', __name__)

# View all sections for a page
@section_bp.route('/<int:page_id>/sections', methods=['GET'])
def manage_sections(page_id):
    page = Page.query.get_or_404(page_id)
    sections = Section.query.filter_by(page_id=page_id).order_by(Section.order).all()
    return render_template('manage_sections.html', page=page, sections=sections)

# Create a new section
@section_bp.route('/<int:page_id>/sections/create', methods=['GET', 'POST'])
def create_section(page_id):
    page = Page.query.get_or_404(page_id)
    form = SectionForm()
    if form.validate_on_submit():
        section = Section(
            page_id=page_id,
            name=form.name.data,
            order=form.order.data
        )
        db.session.add(section)
        db.session.commit()
        flash('Section created successfully!', 'success')
        return redirect(url_for('section_bp.manage_sections', page_id=page_id))
    return render_template('edit_section.html', form=form, page=page)

# Edit a section
@section_bp.route('/sections/<int:section_id>/edit', methods=['GET', 'POST'])
def edit_section(section_id):
    section = Section.query.get_or_404(section_id)
    form = SectionForm(obj=section)
    if form.validate_on_submit():
        section.name = form.name.data
        section.order = form.order.data
        db.session.commit()
        flash('Section updated successfully!', 'success')
        return redirect(url_for('section_bp.manage_sections', page_id=section.page_id))
    return render_template('edit_section.html', form=form, page=section.page)

# Delete a section
@section_bp.route('/sections/<int:section_id>/delete', methods=['POST'])
def delete_section(section_id):
    section = Section.query.get_or_404(section_id)
    page_id = section.page_id
    db.session.delete(section)
    db.session.commit()
    flash('Section deleted successfully!', 'success')
    return redirect(url_for('section_bp.manage_sections', page_id=page_id))

# View all elements for a section
@section_bp.route('/sections/<int:section_id>/elements', methods=['GET'])
def manage_elements(section_id):
    section = Section.query.get_or_404(section_id)
    elements = Element.query.filter_by(section_id=section_id).order_by(Element.order).all()
    return render_template('manage_elements.html', section=section, elements=elements)

# Create a new element
@section_bp.route('/sections/<int:section_id>/elements/create', methods=['GET', 'POST'])
def create_element(section_id):
    section = Section.query.get_or_404(section_id)
    form = ElementForm()
    if form.validate_on_submit():
        element = Element(
            section_id=section_id,
            element_type=form.element_type.data,
            content=form.content.data,
            extra_data=form.extra_data.data,
            order=form.order.data
        )
        db.session.add(element)
        db.session.commit()
        flash('Element created successfully!', 'success')
        return redirect(url_for('section_bp.manage_elements', section_id=section_id))
    return render_template('edit_element.html', form=form, section=section)

# Edit an element
@section_bp.route('/elements/<int:element_id>/edit', methods=['GET', 'POST'])
def edit_element(element_id):
    element = Element.query.get_or_404(element_id)
    form = ElementForm(obj=element)
    if form.validate_on_submit():
        element.element_type = form.element_type.data
        element.content = form.content.data
        element.extra_data = form.extra_data.data
        element.order = form.order.data
        db.session.commit()
        flash('Element updated successfully!', 'success')
        return redirect(url_for('section_bp.manage_elements', section_id=element.section_id))
    return render_template('edit_element.html', form=form, section=element.section)

# Delete an element
@section_bp.route('/elements/<int:element_id>/delete', methods=['POST'])
def delete_element(element_id):
    element = Element.query.get_or_404(element_id)
    section_id = element.section_id
    db.session.delete(element)
    db.session.commit()
    flash('Element deleted successfully!', 'success')
    return redirect(url_for('section_bp.manage_elements', section_id=section_id))