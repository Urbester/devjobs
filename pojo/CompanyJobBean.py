class CompanyJobBean(object):
    def __init__(self, token):
        self.token = token
        self.company = self.get_company()

    def add(self, title, description, salary, location, remote, internship):
        from models import Job
        from devjobs import db
        try:
            j = Job(title, description, salary, location, remote, internship, self.company)
            db.session.add(j)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def get(self, id):
        from models import Job
        try:
            jobs = Job.query.filter_by(owner=self.company.id, id=id).first()
            return jobs
        except Exception as e:
            return False

    def all(self):
        from models import Job
        try:
            jobs = Job.query.filter_by(owner=self.company.id).all()
            return jobs
        except Exception as e:
            return False

    def get_company(self):
        from models import Company
        company = Company.query.filter_by(session_token=self.token).first()
        return company
