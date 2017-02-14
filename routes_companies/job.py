import os

from flask import render_template, session, request, send_from_directory
from markupsafe import Markup

from devjobs import app


@app.route('/c/job/form', methods=['POST'])
def c_job_form():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")
    return render_template("companies/job_form.html")



@app.route('/c/resume/<id>', methods=['POST'])
def c_get_resume(id):
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")

    from pojo import CompanyJobBean
    bean = CompanyJobBean(session["X-Auth-Token"])
    resume_link = bean.get_resume(id)
    if not resume_link:
        return render_template("companies/dashboard.html", alert="You don't have permission.", alert_type="warning")
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads, resume_link)

@app.route('/c/job/<id>', methods=['POST'])
def c_job_show(id):
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")

    from pojo import CompanyJobBean
    bean = CompanyJobBean(session["X-Auth-Token"])
    job = bean.get(id)
    return render_template("companies/job.html", job=job)


@app.route('/c/job/add', methods=['POST'])
def c_job_add():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")

    # verify input

    try:
        title = unicode(Markup(request.form['title']).striptags())
        if len(title) < 10 or len(title) > 120:
            return render_template("companies/job_form.html", alert="Bad title size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/job_form.html", alert="Bad title.", alert_type="warning")
    try:
        description = unicode(Markup(request.form['description']).striptags())
        if len(description) < 10 or len(description) > 1000:
            return render_template("companies/job_form.html", alert="Bad description size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/job_form.html", alert="Bad description.", alert_type="warning")

    try:
        salary = unicode(Markup(request.form['salary']).striptags())
        salary = int(salary)
        if salary <= 0:
            return render_template("companies/job_form.html", alert="Bad salary size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/job_form.html", alert="Bad salary.", alert_type="warning")

    try:
        location = unicode(Markup(request.form['location']).striptags())
        if len(location) < 10 or len(location) > 120:
            return render_template("companies/job_form.html", alert="Bad location size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/job_form.html", alert="Bad location.", alert_type="warning")

    try:
        remote = unicode(Markup(request.form['remote']).striptags())
        remote = True
    except Exception as e:
        remote = False

    try:
        internship = unicode(Markup(request.form['internship']).striptags())
        internship = True
    except Exception as e:
        internship = False

    from pojo import CompanyJobBean
    bean = CompanyJobBean(session["X-Auth-Token"])
    if bean.add(title, description, salary, location, remote, internship):
        jobs = bean.all()
        return render_template("companies/dashboard.html", jobs=jobs, alert="Job published successfully.", alert_type="success")
    else:
        return render_template("companies/dashboard.html", alert="Please try again.", alert_type="warning")
