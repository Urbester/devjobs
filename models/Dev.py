from devjobs import db


class Dev(db.Model):
    __tablename__ = 'dev'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(120), nullable=False)
    resume_link = db.Column(db.String(120), unique=True)

    def __init__(self, email, pwd, resume_link):
        self.email = email
        self.pwd = pwd
        self.resume_link = resume_link
