from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

def db_connector():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:SoftwareProject@spm.czdb9a0r4ea9.ap-southeast-1.rds.amazonaws.com:3306/LJPS_DB'
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/LJPS_DB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
    db = SQLAlchemy(app)
    CORS(app)
    return db