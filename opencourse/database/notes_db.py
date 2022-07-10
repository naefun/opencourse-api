import mongoengine as me

class Note(me.Document):
    user_id = me.StringField(required=True)
    course_id = me.StringField(required=True)
    unit_id = me.StringField(required=True)
    lesson_id = me.StringField(required=True)
    content = me.StringField(required=True)