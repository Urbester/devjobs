from devjobs import app
from flask import render_template


@app.route('/c/settings', methods=['POST'])
def c_settings():
    return render_template("companies/settings.html")


@app.route('/c/me', methods=['POST'])
def c_me():
    return render_template("companies/me.html")
