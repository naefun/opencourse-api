from marshmallow import Schema, fields

class Note():
    def __init__(self, user_id, course_id, unit_id, lesson_id, content):
        self.user_id = user_id
        self.course_id = course_id
        self.unit_id = unit_id
        self.lesson_id = lesson_id
        self.content = content

    def __repr__(self):
        return '<Note(name={self.content!r})>'.format(self=self)

class NoteSchema(Schema):
    user_id = fields.Str()
    course_id = fields.Str()
    unit_id = fields.Str()
    lesson_id = fields.Str()
    content = fields.Str()
    id = fields.Str()