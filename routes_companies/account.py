from devjobs import app
from flask import render_template, session


@app.route('/c/settings', methods=['POST'])
def c_settings():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")
    return render_template("companies/settings.html")


@app.route('/c/dashboard', methods=['POST'])
def c_dashboard():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")

    from pojo import CompanyJobBean
    bean = CompanyJobBean(session["X-Auth-Token"])
    jobs = bean.all()
    return render_template("companies/dashboard.html", jobs=jobs)


@app.route('/c/premium', methods=['GET'])
def c_premium():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")
    return render_template("companies/premium.html")
