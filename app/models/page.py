from ..extensions import db


class Page(db.Model):
    """Модель для хранения страниц."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  # Название страницы
    slug = db.Column(db.String(100), unique=True, nullable=False)  # URL страницы
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    # Связь с секциями
    sections = db.relationship('Section', backref='page', lazy=True, cascade="all, delete-orphan")


class Section(db.Model):
    """Модель для хранения секций страницы."""
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)  # ID страницы
    name = db.Column(db.String(100), nullable=False)  # Имя секции (например, "О нас")
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения секции
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    # Связь с элементами
    elements = db.relationship('Element', backref='section', lazy=True, cascade="all, delete-orphan")


class Element(db.Model):
    """Модель для хранения элементов в секциях."""
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)  # ID секции
    element_type = db.Column(db.String(50), nullable=False)  # Тип элемента: text, image, video, link и т.д.
    content = db.Column(db.Text, nullable=True)  # Основной контент элемента (например, текст, JSON)
    extra_data = db.Column(db.JSON, nullable=True)  # Дополнительные данные (например, URL для видео/ссылки)
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения элемента
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)


class Heading(db.Model):
    """Модель для хранения заголовков на странице."""
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)  # Контент заголовка
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения заголовка
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)
    
    page = db.relationship('Page', backref='headings', lazy=True)


class TextBlock(db.Model):
    """Модель для хранения текстовых блоков на странице."""
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)  # Контент блока текста
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    page = db.relationship('Page', backref='text_blocks', lazy=True)


class Link(db.Model):
    """Модель для хранения ссылок на странице."""
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)  # URL ссылки
    title = db.Column(db.String(100), nullable=False)  # Заголовок ссылки
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    page = db.relationship('Page', backref='links', lazy=True)


class Media(db.Model):
    """Модель для хранения медиа-файлов на странице."""
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)  # Путь к файлу
    file_type = db.Column(db.String(50), nullable=False)  # Тип файла (например, 'image', 'video', и т.д.)
    order = db.Column(db.Integer, nullable=False, default=0)  # Порядок отображения
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    page = db.relationship('Page', backref='media', lazy=True)


