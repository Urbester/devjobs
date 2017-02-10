from devjobs import db
from models import job_applications


class Dev(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(120), nullable=False)
    resume_link = db.Column(db.String(120), unique=True)
    session_token = db.Column(db.String(256), unique=True)
    job_applications = db.relationship('Job', secondary=job_applications, backref=db.backref('applied_jobs', lazy='dynamic'))

    def __init__(self, email, pwd, resume_link):
        self.email = email
        self.pwd = pwd
        self.resume_link = resume_link
        from utils import generate_token
        self.session_token = unicode(generate_token())
