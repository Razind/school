from flask import Flask, flash
from .extensions import db, migrate
from .config import Config
from flask_login import LoginManager
from .models.user import User  # Импортируйте модель User
from sqlalchemy import text


from .routes.user import user_bp
from .routes.post import post
from .routes.Iato import iato
from .routes.shlive import shlive
from .routes.klassi import klassi
from .routes.ychit import ychit
from .routes.question import question_bp

def create_app(config_class=Config): 
    app = Flask(__name__)
    app.config.from_object(config_class)
    

    # Определение функции nl2br
    def nl2br(value):
        return value.replace('\n', '<br>\n')

    # Регистрация фильтра в приложении Flask
    app.jinja_env.filters['nl2br'] = nl2br

    app.register_blueprint(user_bp)
    app.register_blueprint(post)
    app.register_blueprint(iato)
    app.register_blueprint(shlive)
    app.register_blueprint(klassi)
    app.register_blueprint(ychit)
    app.register_blueprint(question_bp)
    

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

        # Добавьте тестовый запрос для проверки подключения к базе данных
        try:
            result = db.session.execute(text('SELECT 1'))
            print(f"Database connection test passed: {result.fetchone()}")
        except Exception as e:
            print(f"Database connection test failed: {e}")

    return app
