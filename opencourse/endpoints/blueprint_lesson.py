from flask import Blueprint, jsonify, request
from services.lesson import get_lessons, get_lesson_by_id, create_lesson

blueprint_lesson = Blueprint("blueprint_lesson", __name__)

@blueprint_lesson.route('/lessons')
def get_all_lessons():
  return jsonify(get_lessons(request.args))

@blueprint_lesson.route('/lessons/<id>')
def get_single_lesson(id):
  return jsonify(get_lesson_by_id(id))

@blueprint_lesson.route('/lessons', methods=['POST'])
def add_lesson():
  lesson = create_lesson(request)
  return jsonify(lesson), 204