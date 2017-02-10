from devjobs import app
from flask import render_template


@app.route('/')
def index():
    return render_template("devs/index.html")


@app.route('/enter')
def enter():
    return render_template("devs/login.html", alert="", alert_type="")
