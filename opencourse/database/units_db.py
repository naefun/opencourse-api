import mongoengine as me

class Unit(me.Document):
    course_id = me.StringField(required=True)
    position = me.IntField()
    title = me.StringField()