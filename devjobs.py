from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
from routes_devs import *
from routes_companies import *
from error_handlers import *

UPLOAD_FOLDER = '/Users/alizardo/PycharmProjects/devjobs/uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'devJobsSideProject2017'

if __name__ == '__main__':
    try:
        from models import *
        db.create_all()
        db.session.commit()
    except Exception as e:
        print e
    app.run()
