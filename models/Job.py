from devjobs import db

job_dev_applications = db.Table('Job_Applications',
                                db.Column('job_id', db.Integer, db.ForeignKey('Job.id'), primary_key=True),
                                db.Column('dev_id', db.Integer, db.ForeignKey('Dev.id'), primary_key=True)
                                )


class Job(db.Model):
    __tablename__ = "Job"

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column("title", db.String(120), unique=True)
    description = db.Column("description", db.String(1000), nullable=False)
    salary = db.Column("salary", db.Integer)
    open = db.Column("open", db.Boolean, default=True)
    address = db.Column("address", db.Column(db.String(200)))
    remote = db.Column("remote", db.Boolean, default=False)
    internship = db.Column("internship", db.Boolean, default=False)
    applications = db.relationship('Dev', secondary=job_dev_applications,
                                   backref=db.backref('developers', lazy='dynamic'))

    def __init__(self, email, pwd, resume_link):
        self.email = email
        self.pwd = pwd
        self.resume_link = resume_link
        from utils import generate_token
        self.session_token = unicode(generate_token())
