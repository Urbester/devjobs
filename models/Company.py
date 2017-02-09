from devjobs import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    public_email = db.Column(db.String(120), unique=True)
    public_site = db.Column(db.String(120), unique=True)

    def __init__(self, email, pwd, description, public_email, public_site, name):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.description = description
        self.public_email = public_email
        self.public_site = public_site

    def __repr__(self):
        return self.name + " - " + self.email
