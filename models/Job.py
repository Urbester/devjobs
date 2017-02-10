from devjobs import db

job_applications = db.Table('job_applications',
                            db.Column("job_id", db.Integer, db.ForeignKey('job.id')),
                            db.Column("dev_id", db.Integer, db.ForeignKey('dev.id'))
                            )


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    salary = db.Column(db.Integer, default=0)
    closed = db.Column(db.Boolean, default=False)
    location = db.Column(db.String(200))
    remote_work = db.Column(db.Boolean, default=False)
    internship = db.Column(db.Boolean, default=False)
    # the owner
    owner = db.Column(db.Integer, db.ForeignKey('company.id'))
    # developers who applied to this job
    dev_applications = db.relationship('Dev', secondary=job_applications,
                                       backref=db.backref('developers', lazy='dynamic'))

    def __init__(self, title, description, salary, location, remote, internship, owner):
        self.title = title
        self.description = description
        self.salary = salary
        self.location = location
        self.remote_work = remote
        self.internship = internship
        self.owner = owner.id
