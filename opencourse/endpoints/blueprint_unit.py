from flask import Blueprint, jsonify, request
from services.unit import get_units, get_unit_by_id, create_unit

blueprint_unit = Blueprint("blueprint_unit", __name__)


@blueprint_unit.route('/units')
def get_all_units():
    return jsonify(get_units(request.args))


@blueprint_unit.route('/units/<id>')
def get_single_unit(id):
    return jsonify(get_unit_by_id(id))


@blueprint_unit.route('/units', methods=['POST'])
def add_lesson():
    unit = create_unit(request)
    return jsonify(unit), 204
