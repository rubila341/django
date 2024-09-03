from flask import Blueprint, request, jsonify
from app import db
from app.models.response import Response
from app.schemas.response import ResponseCreate, ResponseResponse

bp = Blueprint('responses', __name__, url_prefix='/responses')

@bp.route('', methods=['POST'])
def create_response():
    try:
        data = request.json
        schema = ResponseCreate(**data)
        new_response = Response(text=schema.text, question_id=schema.question_id)
        db.session.add(new_response)
        db.session.commit()
        return jsonify(ResponseResponse.from_orm(new_response).dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:response_id>', methods=['GET'])
def get_response(response_id):
    try:
        response = Response.query.get(response_id)
        if not response:
            return jsonify({'error': 'Response not found'}), 404
        return jsonify(ResponseResponse.from_orm(response).dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
