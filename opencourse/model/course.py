from marshmallow import Schema, fields

class Course():
    def __init__(self, title, description, units):
        self.title = title
        self.description = description
        self.units = units

    def __repr__(self):
        return '<Course(name={self.description!r})>'.format(self=self)

class CourseSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    units = fields.List(fields.Dict())
    id = fields.Str()