from flask import Blueprint, jsonify

blueprint_base = Blueprint('blueprint_base', __name__)

@blueprint_base.route('/')
def get_base():
  output = {"msg": "I'm the base endpoint"}
  return jsonify(output)