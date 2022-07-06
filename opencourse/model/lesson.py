from marshmallow import Schema, fields

class Lesson():
    def __init__(self, unit_id, lesson_position, youtube_video_id, lesson_title):
        self.unit_id = unit_id
        self.lesson_position = lesson_position
        self.youtube_video_id = youtube_video_id
        self.lesson_title = lesson_title

    def __repr__(self):
        return '<Lesson(name={self.description!r})>'.format(self=self)

class LessonSchema(Schema):
    unit_id = fields.Str()
    lesson_position = fields.Integer()
    youtube_video_id = fields.Str()
    lesson_title = fields.Str()