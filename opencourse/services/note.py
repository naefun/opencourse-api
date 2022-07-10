from bson import ObjectId
from model.note import NoteSchema
from database.notes_db import Note


def get_notes(args):
    notes = {}
    lesson_id = args.get("lessonId", default="")
    user_id = args.get("userId", default="")
    if lesson_id != "" and user_id != "":
        notes = get_note_by_user_id_and_lesson_id(lesson_id, user_id)
    return notes


def get_all_notes():
    schema = NoteSchema(many=True)
    notes = schema.dump(Note.objects())
    return notes


def get_note_by_id(id):
    schema = NoteSchema()
    notes = schema.dump(Note.objects(id=ObjectId(id)).first())
    return notes

def get_note_by_user_id_and_lesson_id(lesson_id, user_id):
    schema = NoteSchema()
    notes = schema.dump(Note.objects(lesson_id=lesson_id, user_id=user_id).first())
    return notes


def create_note(request):
    note_obj = NoteSchema().load(request.get_json())
    note = Note(
        user_id=note_obj["user_id"],
        course_id = note_obj["course_id"],
        unit_id = note_obj["unit_id"],
        lesson_id = note_obj["lesson_id"],
        content = note_obj["content"]
    )
    note.save()
    print(note_obj)
    return note

def update_note(request):
    note_obj = NoteSchema().load(request.get_json())
    note = Note(
        id=note_obj["id"],
        user_id=note_obj["user_id"],
        course_id = note_obj["course_id"],
        unit_id = note_obj["unit_id"],
        lesson_id = note_obj["lesson_id"],
        content = note_obj["content"]
    )
    note.save()
    print(note_obj)
    return note
