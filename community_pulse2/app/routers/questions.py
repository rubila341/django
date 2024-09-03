# routers/questions.py
from flask import Blueprint, request, jsonify
from app import db
from app.models.questions import Question, Category
from app.schemas.question import QuestionCreate, QuestionResponse

bp = Blueprint('questions', __name__, url_prefix='/questions')

@bp.route('', methods=['POST'])
def create_question():
    try:
        data = request.json
        schema = QuestionCreate(**data)
        category = Category.query.get(schema.category_id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        new_question = Question(
            title=schema.title,
            description=schema.description,
            category_id=schema.category_id
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify(QuestionResponse.from_orm(new_question).dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('', methods=['GET'])
def get_questions():
    try:
        questions = Question.query.all()
        return jsonify([QuestionResponse.from_orm(q).dict() for q in questions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
