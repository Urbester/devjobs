from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
from routes import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)
from models import *


if __name__ == '__main__':
    app.run()
