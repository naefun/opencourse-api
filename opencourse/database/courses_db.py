import mongoengine as me

class Course(me.Document):
    title = me.StringField(required=True)
    description = me.StringField()
    units = me.ListField()