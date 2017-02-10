import os

from markupsafe import Markup
from werkzeug.utils import secure_filename

from devjobs import app
from flask import render_template, request

from utils import allowed_file


@app.route('/login', methods=['POST'])
def login_form():
    try:
        email = unicode(Markup(request.form['email']).striptags())
        if len(email) < 10 or len(email) > 120:
            return render_template("devs/login.html", alert="Bad email size.", alert_type="warning")
    except Exception as e:
        return render_template("devs/login.html", alert="Bad email.", alert_type="warning")
    try:
        password = unicode(Markup(request.form['pwd']).striptags())
        if len(password) < 10 or len(password) > 120:
            return render_template("devs/login.html", alert="Bad password size.", alert_type="warning")
    except Exception as e:
        return render_template("devs/login.html", alert="Bad password.", alert_type="warning")
    from pojo import DevAuthBean
    bean = DevAuthBean()
    if bean.login(email, password):
        return render_template("devs/dashboard.html")
    else:
        return render_template("devs/login.html", alert="Bad credentials.", alert_type="warning")


@app.route('/register', methods=['POST'])
def register_form():
    try:
        email = unicode(Markup(request.form['email']).striptags())
        if len(email) < 10 or len(email) > 120:
            return render_template("devs/register.html", alert="Bad email size.", alert_type="warning")
    except Exception as e:
        return render_template("devs/register.html", alert="Bad email.", alert_type="warning")
    try:
        password = unicode(Markup(request.form['pwd']).striptags())
        if len(password) < 10 or len(password) > 120:
            return render_template("devs/register.html", alert="Bad password size.", alert_type="warning")
    except Exception as e:
        return render_template("register.html", alert="Bad password.", alert_type="warning")
    try:
        if 'resume' not in request.files:
            return render_template("register.html", alert="Bad resume.", alert_type="warning")
        file = request.files['resume']
        if file.filename == '':
            return render_template("register.html", alert="Bad resume name.", alert_type="warning")
        if file and allowed_file(file.filename):
            filename = secure_filename(email + file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except Exception as e:
        return render_template("devs/register.html", alert="Bad resume.", alert_type="warning")

    from pojo import DevAuthBean
    bean = DevAuthBean()
    if bean.register(email, password, filename):
        return render_template("devs/register.html", alert="Account created.", alert_type="success")
    else:
        return render_template("devs/register.html", alert="Account already registered.", alert_type="warning")

@app.route('/register')
def register():
    return render_template("devs/register.html")


@app.route('/logout', methods=['POST'])
def logout():
    return render_template("devs/index.html")
