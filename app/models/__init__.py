from flask_sqlalchemy import SQLAlchemy

# Создаем объект SQLAlchemy
db = SQLAlchemy()

# Импортируем модели
from .user import User
from .page import Page, Section, Element, Heading, TextBlock, Link, Media
from .post import Post
from .question import Question
