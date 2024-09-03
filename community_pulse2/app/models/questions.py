from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(512), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Добавлено

    category = db.relationship('Category', back_populates='questions')  # Добавлено

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    questions = db.relationship('Question', back_populates='category')  # Добавлено
