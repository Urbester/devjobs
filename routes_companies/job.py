from flask import render_template, session

from devjobs import app


@app.route('/c/job/form', methods=['POST'])
def c_job_form():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")
    return render_template("companies/job_form.html")
