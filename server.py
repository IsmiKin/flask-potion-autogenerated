import logging
import os
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, Resource
# from flasgger import Swagger

from database.potion_resources import *

logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
log = logging.getLogger()
log.setLevel(logging.INFO)

fileHandler = logging.FileHandler('/var/log/pinfo.log')
fileHandler.setFormatter(logFormatter)
log.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

app = Flask(__name__)


def configure_app(flask_app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://{}:{}@mysql/{}'.format(os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'], os.environ['DB_SCHEMA'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


def initialize_app(flask_app):
    configure_app(flask_app)

    api = Api(app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)

    api.add_resource(CampaignResource)
    api.add_resource(Resource)

    # Swagger(app)

    db.init_app(flask_app)


@app.route('/')
def index():
    return jsonify({"message": "pika"})

if __name__ == "__main__":
    initialize_app(app)
    app.run(host='0.0.0.0', port=4333, debug=os.environ['ENV'] != 'prod')
