from flask import Blueprint, jsonify, request
from services.note import get_notes, create_note, get_note_by_id, update_note

blueprint_note = Blueprint("blueprint_note", __name__)


@blueprint_note.route('/notes')
def retrieve_notes():
    return jsonify(get_notes(request.args))


@blueprint_note.route('/notes/<id>')
def get_single_note(id):
    return jsonify(get_note_by_id(id))


@blueprint_note.route('/notes', methods=['POST'])
def add_note():
    note = create_note(request)
    return jsonify(note)

@blueprint_note.route('/notes', methods=['PUT'])
def change_note():
    note = update_note(request)
    return jsonify(note)