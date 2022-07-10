from bson import ObjectId
from model.course import CourseSchema
from database.courses_db import Course
import logging


def get_courses(args):
    # courses = {}
    # user_id = args.get("user_id", default="")
    # if user_id != "":
    #     courses = get_courses_by_user_id(user_id)
    # else:
    #     courses = get_all_courses()

    courses = get_all_courses()
    return courses


def get_all_courses():
    schema = CourseSchema(many=True)
    courses = schema.dump(Course.objects())
    return courses


def get_course_by_id(id):
    schema = CourseSchema()
    courses = schema.dump(Course.objects(id=ObjectId(id)).first())
    return courses

# needs to be implemented, but this should get all courses from a user
# def get_courses_by_user_id(id):
#     schema = CourseSchema(many=True)
#     courses = schema.dump(
#         filter(lambda course: course.course_id == id, Course.objects())
#     )
#     return courses


def create_course(request):
    course_obj = CourseSchema().load(request.get_json())
    course = Course(title=course_obj["title"], description=course_obj["description"], units=course_obj["units"])
    course.save()
    return course

def update_course(request, id):
    course_obj = CourseSchema().load(request.get_json())
    course = Course(title=course_obj["title"], description=course_obj["description"], units=course_obj["units"], id=id)
    course.save()
    return course
