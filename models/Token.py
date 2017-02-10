from devjobs import db


class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(256), unique=True)

    id_dev = db.Column(db.Integer, db.ForeignKey('dev.id'))
    dev = db.relationship('dev',
        backref=db.backref('devs', lazy='dynamic'))

    def __init__(self, dev):
        self.id_dev = dev.id
        from utils import generate_token
        self.token = unicode(generate_token())