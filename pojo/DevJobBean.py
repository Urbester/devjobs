class DevJobBean(object):
    def __init__(self, token):
        self.token = token
        self.dev = self.get_dev()

    def query(self, query):
        from models import Job
        try:
            jobs = Job.query.filter(Job.title.like("%"+query+"%")).filter_by(closed=False).all()
            return jobs
        except Exception as e:
            return False

    def all(self):
        from models import Job
        try:
            jobs = Job.query.filter_by(owner=self.dev.id).all()
            return jobs
        except Exception as e:
            return False

    def get_dev(self):
        from models import Dev
        dev = Dev.query.filter_by(session_token=self.token).first()
        return dev
