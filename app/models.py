from app import app
from flask import jsonify, json, request
from ..database import dboperations


db = dboperations.DbOperations

class Models():
    @app.route('/api/v1/questions', methods=['GET'])
    def all_questions():
        questions = db.get_all_questions()
        return jsonify(questions), 200