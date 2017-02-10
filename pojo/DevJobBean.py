class DevJobBean(object):
    def __init__(self, token):
        self.token = token
        self.dev = self.get_dev()

    def query(self, query):
        from models import Job
        try:
            jobs = Job.query.filter(Job.title.like("%" + query + "%")).filter_by(closed=False).all()
            return jobs
        except Exception as e:
            return False

    def get_owner(self, id):
        from models import Job, Company
        try:
            jobs = Job.query.filter_by(id=id, closed=False).first()
            owner = Company.query.filter_by(id=jobs.owner).first()
            return owner
        except Exception as e:
            return False

    def apply(self, id):
        from models import Job
        from devjobs import db
        try:
            jobs = Job.query.filter_by(id=id, closed=False).first()
            self.dev.job_applications.append(jobs)
            return True
        except Exception as e:
            return False

    def get(self, id):
        from models import Job
        try:
            jobs = Job.query.filter_by(id=id, closed=False).first()
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
