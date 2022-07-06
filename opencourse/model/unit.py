from marshmallow import Schema, fields

class Unit():
    def __init__(self, course_id, position, title):
        self.course_id = course_id
        self.position = position
        self.title = title

    def __repr__(self):
        return '<Unit(name={self.description!r})>'.format(self=self)

class UnitSchema(Schema):
    course_id = fields.Str()
    position = fields.Integer()
    title = fields.Str()
    id = fields.Str()