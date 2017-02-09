from Dev import Dev
from devjobs import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    salary = db.Column(db.Integer, default=0)
    location = db.Column(db.String(50), nullable=False)
    remote = db.Column(db.Boolean, default=False)
    junior = db.Column(db.Boolean, default=False)
    internship = db.Column(db.Boolean, default=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __init__(self, title, description, salary, location, remote, junior, internship, company_id):
        self.title = title
        self.description = description
        self.salary = salary
        self.location = location
        self.remote = remote
        self.junior = junior
        self.internship = internship
        self.company_id = company_id

    def __repr__(self):
        return self.title
