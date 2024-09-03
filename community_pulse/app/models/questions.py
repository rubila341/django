from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='questions')
    responses = db.relationship('Response', backref='question', lazy=True)

    def __repr__(self):
        return f'<Question {self.title}>'
