from markupsafe import Markup

from devjobs import app
from flask import render_template, session, request


@app.route('/search', methods=['POST'])
def search():
    from pojo import DevAuthBean
    bean = DevAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("devs/index.html")
    try:
        query = unicode(Markup(request.form['query']).striptags())
        if len(query) < 0 or len(query) > 120:
            return render_template("devs/search.html", alert="Bad query size.", alert_type="warning")
    except Exception as e:
        return render_template("devs/search.html")

    from pojo import DevJobBean
    bean = DevJobBean(session["X-Auth-Token"])
    jobs = bean.query(query)
    return render_template("devs/search.html", results=jobs)
