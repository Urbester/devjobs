import os

from markupsafe import Markup
from werkzeug.utils import secure_filename

from devjobs import app
from flask import render_template, request

from utils import allowed_file


@app.route('/c/login', methods=['POST'])
def c_login_form():
    try:
        email = unicode(Markup(request.form['email']).striptags())
        if len(email) < 10 or len(email) > 120:
            return render_template("companies/login.html", alert="Bad email size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/login.html", alert="Bad email.", alert_type="warning")
    try:
        password = unicode(Markup(request.form['pwd']).striptags())
        if len(password) < 10 or len(password) > 120:
            return render_template("companies/login.html", alert="Bad password size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/login.html", alert="Bad password.", alert_type="warning")
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if bean.login(email, password):
        return render_template("companies/dashboard.html")
    else:
        return render_template("companies/login.html", alert="Bad credentials.", alert_type="warning")


@app.route('/c/register', methods=['POST'])
def c_register_form():
    try:

        email = unicode(Markup(request.form['email']).striptags())
        if len(email) < 10 or len(email) > 120:
            return render_template("companies/register.html", alert="Bad email size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/register.html", alert="Bad email.", alert_type="warning")
    try:
        password = unicode(Markup(request.form['pwd']).striptags())
        if len(password) < 10 or len(password) > 120:
            return render_template("companies/register.html", alert="Bad password size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/register.html", alert="Bad password.", alert_type="warning")
    try:
        description = unicode(Markup(request.form['description']).striptags())
        if len(description) < 15 or len(description) > 500:
            return render_template("companies/register.html", alert="Bad description size.", alert_type="warning")
    except Exception as e:
        return render_template("companies/register.html", alert="Bad description.", alert_type="warning")

    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if bean.register(email, password, description):
        return render_template("companies/register.html", alert="Account created.", alert_type="success")
    else:
        return render_template("companies/register.html", alert="Account already registered.", alert_type="warning")

@app.route('/c/register')
def c_register():
    return render_template("companies/register.html")


@app.route('/c/logout', methods=['POST'])
def c_logout():
    return render_template("companies/index.html")
