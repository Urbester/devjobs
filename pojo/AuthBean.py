class AuthBean(object):
    def __init__(self):
        pass

    def register_dev(self, email, pwd, filename):
        from models import Dev
        from devjobs import db
        from hashlib import sha512

        try:
            user = Dev(email, sha512(pwd).hexdigest(), filename)
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def login_dev(self, email, pwd):
        from models import Dev
        from devjobs import db, session
        from hashlib import sha512
        from utils import generate_token

        try:
            # get user
            u = Dev.query.filter_by(email=email, pwd=sha512(pwd).hexdigest()).first()
            if u is None:
                return False
            u.session_token = unicode(generate_token())
            db.session.commit()

            session["email"] = u.email
            session["X-Auth-Token"] = u.session_token

            return True
        except Exception as e:
            return False