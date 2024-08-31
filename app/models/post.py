from ..extensions import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    content = db.Column(db.String(5000))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(200))