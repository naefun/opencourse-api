import logging
from os import environ
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
mongodb_db = environ.get('MONGODB_DB', 'opencourse')
mongodb_host = environ.get('MONGODB_HOST', 'localhost')
mongodb_port = environ.get('MONGODB_PORT', 27017)
mongodb_user = environ.get('MONGODB_USER', 'root')
mongodb_pass = environ.get('MONGODB_PASS', 'rootpassword')

app.config['MONGODB_SETTINGS'] = {
    'db': mongodb_db,
    'host': mongodb_host,
    'port': mongodb_port,
    'username': mongodb_user,
    'password': mongodb_pass
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
  serve(TransLogger(app, setup_console_handler=True),host='0.0.0.0', port=5000)