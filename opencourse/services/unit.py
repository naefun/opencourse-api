from bson import ObjectId
from model.unit import UnitSchema
from database.units_db import Unit


def get_units(args):
    units = {}
    unit_id = args.get("course_id", default="")
    if unit_id != "":
        units = get_units_by_course_id(unit_id)
    else:
        units = get_all_units()
    return units


def get_all_units():
    schema = UnitSchema(many=True)
    units = schema.dump(Unit.objects())
    return units


def get_unit_by_id(id):
    schema = UnitSchema()
    units = schema.dump(Unit.objects(id=ObjectId(id)).first())
    return units


def get_units_by_course_id(id):
    schema = UnitSchema(many=True)
    units = schema.dump(
        filter(lambda unit: unit.unit_id == id, Unit.objects())
    )
    return units


def create_unit(request):
    unit_obj = UnitSchema().load(request.get_json())
    unit = Unit(course_id=unit_obj["course_id"], title=unit_obj["title"],
                position=unit_obj["position"])
    unit.save()
    print(unit_obj)
    return unit
