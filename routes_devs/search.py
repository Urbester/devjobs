from devjobs import app
from flask import render_template, session


@app.route('/search', methods=['POST'])
def search():
    from pojo import DevAuthBean
    bean = DevAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("devs/index.html")
    return render_template("devs/search.html")
