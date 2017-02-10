from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
from routes import *

UPLOAD_FOLDER = '/Users/alizardo/PycharmProjects/devjobs/uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

#memory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

try:
    from models import *
    db.create_all()
    db.session.commit()
except Exception as e:
    print e

if __name__ == '__main__':
    app.run()
