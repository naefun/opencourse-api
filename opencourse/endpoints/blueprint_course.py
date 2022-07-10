from flask import Blueprint, jsonify, request
from services.course import get_courses, create_course, get_course_by_id, update_course

blueprint_course = Blueprint("blueprint_course", __name__)


@blueprint_course.route('/courses')
def get_all_courses():
    return jsonify(get_courses(request.args))


@blueprint_course.route('/courses/<id>')
def get_single_course(id):
    return jsonify(get_course_by_id(id))


@blueprint_course.route('/courses', methods=['POST'])
def add_course():
    course = create_course(request)
    return jsonify(course)

@blueprint_course.route('/courses/<id>', methods=['PUT'])
def change_course(id):
    course = update_course(request, id)
    return jsonify(course)