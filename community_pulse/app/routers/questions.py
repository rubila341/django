from flask import Blueprint, request, jsonify
from app import db
from app.models.questions import Question
from app.models.response import Response
from app.schemas.question import QuestionCreate, QuestionResponse
from app.schemas.response import ResponseCreate, ResponseResponse

bp = Blueprint('questions', __name__, url_prefix='/questions')

@bp.route('', methods=['POST'])
def create_question():
    try:
        data = request.json
        schema = QuestionCreate(**data)
        new_question = Question(title=schema.title, description=schema.description)
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
