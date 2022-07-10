import logging
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from waitress import serve
from paste.translogger import TransLogger
from endpoints.blueprint_base import blueprint_base
from endpoints.blueprint_lesson import blueprint_lesson
from endpoints.blueprint_unit import blueprint_unit
from endpoints.blueprint_course import blueprint_course
from endpoints.blueprint_note import blueprint_note

app = Flask(__name__)

#mongodb setup
app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': 'localhost',
    'port': 27017,
    'username':'root',
    'password':'rootpassword'
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()

#logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

#CORS
CORS(app)

#endpoints
versioned_url_prefix = "/api/v1"
app.register_blueprint(blueprint_base, url_prefix = versioned_url_prefix)
app.register_blueprint(blueprint_lesson, url_prefix = versioned_url_prefix)
app.register_blueprint(blueprint_unit, url_prefix = versioned_url_prefix)
app.register_blueprint(blueprint_course, url_prefix = versioned_url_prefix)
app.register_blueprint(blueprint_note, url_prefix = versioned_url_prefix)

#waitress server
if __name__ == "__main__":
  serve(TransLogger(app, setup_console_handler=True), port=5000)