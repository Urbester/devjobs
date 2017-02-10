from devjobs import app
from flask import render_template, session


@app.route('/settings', methods=['POST'])
def settings():
    from pojo import DevAuthBean
    bean = DevAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("devs/index.html")
    return render_template("devs/settings.html")


@app.route('/dashboard', methods=['POST'])
def dashboard():
    from pojo import DevAuthBean
    bean = DevAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("devs/index.html")
    from pojo import DevJobBean
    bean = DevJobBean(session["X-Auth-Token"])
    jobs = bean.get_applied()
    return render_template("devs/dashboard.html", jobs=jobs)
