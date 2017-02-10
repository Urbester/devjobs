from devjobs import app
from flask import render_template, session


@app.route('/c/')
def c_index():
    return render_template("companies/index.html")


@app.route('/c/enter')
def c_enter():
    return render_template("companies/login.html", alert="", alert_type="")
