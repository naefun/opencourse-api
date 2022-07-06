import mongoengine as me

class Lesson(me.Document):
    unit_id = me.StringField(required=True)
    lesson_position = me.IntField()
    youtube_video_id = me.StringField()
    lesson_title = me.StringField()