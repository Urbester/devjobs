class DevJobBean(object):
    def __init__(self, token):
        self.token = token
        self.dev = self.get_dev()

    def query(self, query):
        from models import Job
        try:
            query = query.split(",")
            remote = False
            internship = False
            for i in range(0, len(query)):
                query[i] = query[i].upper().strip()
            if "REMOTE" in query:
                remote = True
            if "INTERNSHIP" in query:
                internship = True
            if remote and internship and len(query) == 4:
                location = query[1]
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%")).filter(Job.location.ilike("%" + location + "%"))\
                    .filter_by(closed=False, remote_work=True, internship=True).all()
            if remote and internship and len(query) == 3:
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%"))\
                    .filter_by(closed=False, remote_work=True, internship=True).all()
            elif remote and len(query) == 3:
                location = query[1]
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%")).filter(Job.location.ilike("%" + location + "%"))\
                    .filter_by(closed=False, remote_work=True).all()
            elif internship and len(query) == 3:
                location = query[1]
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%")).filter(Job.location.ilike("%" + location + "%"))\
                    .filter_by(closed=False, internship=True).all()
            elif len(query) == 2 and internship:
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%"))\
                    .filter_by(closed=False, internship=True).all()
            elif len(query) == 2 and remote:
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%"))\
                    .filter_by(closed=False, remote_work=True).all()
            elif len(query) == 2 and not remote and not internship:
                location = query[1]
                query = query[0]
                jobs = Job.query.filter(Job.title.ilike("%" + query + "%")).filter(Job.location.ilike("%" + location + "%"))\
                    .filter_by(closed=False).all()
            else:
                jobs = Job.query.filter(Job.title.ilike("%" + query[0] + "%"))\
                    .filter_by(closed=False).all()
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
            jobs.dev_applications.append(self.dev)
            db.session.commit()
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

    def get_applied(self):
        return self.dev.job_applications