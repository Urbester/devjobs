from devjobs import db

applies = db.Table('applies',
                   db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
                   db.Column('dev_id', db.Integer, db.ForeignKey('dev.id'))
                   )


class Dev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(120), nullable=False)
    resume_link = db.Column(db.String(120), unique=True)

    applies = db.relationship('Job', secondary=applies,
                              backref=db.backref('devs', lazy='dynamic'))

    def __init__(self, email, pwd, resume_link):
        self.email = email
        self.pwd = pwd
        self.resume_link = resume_link

    def __repr__(self):
        return self.email
