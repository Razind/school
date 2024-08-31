from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models.question import Question

question_bp = Blueprint('question', __name__)

@question_bp.route('/faq', methods=['GET', 'POST'])
def faq():
    print("Method:", request.method)
    if request.method == 'POST':
        full_name = request.form['fullName']
        email = request.form['email']
        question_text = request.form['question']

        new_question = Question(full_name=full_name, email=email, question=question_text)
        db.session.add(new_question)
        db.session.commit()

        flash('Ваш вопрос успешно отправлен!', 'success')
        return redirect(url_for('question.faq'))

    return render_template('faq.html')

@question_bp.route('/questions', methods=['GET'])
def list_questions():
    questions = Question.query.order_by(Question.date_created.desc()).all()
    num_questions = len(questions)  # Получение количества вопросов
    return render_template('admin/questions.html', questions=questions, num_questions=num_questions)


@question_bp.route('/question/<int:id>/delete', methods=['POST'])
def delete_question(id):
    question = Question.query.get(id)
    if question is None:
        flash('Вопрос не найден!', 'danger')
        return redirect(url_for('question.list_questions'))

    try:
        db.session.delete(question)
        db.session.commit()
        flash('Вопрос успешно удален!', 'success')
    except Exception as e:
        db.session.rollback()  # Вернуть транзакцию в исходное состояние
        flash(f'Ошибка при удалении вопроса: {str(e)}', 'danger')

    return redirect(url_for('question.list_questions'))

