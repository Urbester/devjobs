from devjobs import db


class Company(db.Model):
    __tablename__ = "Company"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    email = db.Column("email", db.String(120), unique=True)
    pwd = db.Column("pwd", db.String(120), nullable=False)
    description = db.Column("description", db.String(500), unique=True)
    session_token = db.Column("session_token", db.String(256), unique=True)
    premium = db.Column("premium", db.Boolean, default=False)

    def __init__(self, email, pwd, description):
        self.email = email
        self.pwd = pwd
        self.description = description
        from utils import generate_token
        self.session_token = unicode(generate_token())
