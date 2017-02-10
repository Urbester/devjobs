from devjobs import db
from models import job_dev_applications


class Dev(db.Model):
    __tablename__ = "Dev"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    email = db.Column("email", db.String(120), unique=True)
    pwd = db.Column("pwd", db.String(120), nullable=False)
    resume_link = db.Column("resume_link", db.String(120), unique=True)
    session_token = db.Column("session_token", db.String(256), unique=True)
    applications = db.relationship('Job', secondary=job_dev_applications, backref=db.backref('jobs', lazy='dynamic'))

    def __init__(self, email, pwd, resume_link):
        self.email = email
        self.pwd = pwd
        self.resume_link = resume_link
        from utils import generate_token
        self.session_token = unicode(generate_token())
