from bson import ObjectId
from model.lesson import LessonSchema
from database.lessons_db import Lesson


def get_lessons(args):
    lessons = {}
    unit_id = args.get("unit_id", default="")
    if unit_id != "":
        lessons = get_lessons_by_unit_id(unit_id)
    else:
        lessons = get_all_lessons()
    return lessons


def get_all_lessons():
    schema = LessonSchema(many=True)
    lessons = schema.dump(Lesson.objects())
    return lessons


def get_lesson_by_id(id):
    schema = LessonSchema()
    lessons = schema.dump(Lesson.objects(id=ObjectId(id)).first())
    return lessons


def get_lessons_by_unit_id(id):
    schema = LessonSchema(many=True)
    lessons = schema.dump(
        filter(lambda lesson: lesson.unit_id == id, Lesson.objects())
    )
    return lessons


def create_lesson(request):
    lesson_obj = LessonSchema().load(request.get_json())
    lesson = Lesson(unit_id=lesson_obj["unit_id"], lesson_title=lesson_obj["lesson_title"],
                    youtube_video_id=lesson_obj["youtube_video_id"], lesson_position=lesson_obj["lesson_position"])
    lesson.save()
    print(lesson_obj)
    return lesson
