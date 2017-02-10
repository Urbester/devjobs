from devjobs import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/enter')
def enter():
    return render_template("login.html", alert="", alert_type="")
