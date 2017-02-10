class CompanyAuthBean(object):
    def __init__(self):
        pass

    def register(self, email, pwd, description):
        from models import Company
        from devjobs import db
        from hashlib import sha512

        try:
            c = Company(email, sha512(pwd).hexdigest(), description)
            db.session.add(c)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def login(self, email, pwd):
        from models import Company
        from devjobs import db, session
        from hashlib import sha512
        from utils import generate_token

        try:
            # get user
            u = Company.query.filter_by(email=email, pwd=sha512(pwd).hexdigest()).first()
            if u is None:
                return False
            u.session_token = unicode(generate_token())
            db.session.commit()

            session["email"] = u.email
            session["X-Auth-Token"] = u.session_token

            return True
        except Exception as e:
            return False