from devjobs import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), unique=True)
    session_token = db.Column(db.String(256), unique=True)
    premium = db.Column(db.Boolean, default=False)

    def __init__(self, email, pwd, description):
        self.email = email
        self.pwd = pwd
        self.description = description
        from utils import generate_token
        self.session_token = unicode(generate_token())
