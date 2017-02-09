from devjobs import app
from flask import render_template


@app.route('/settings', methods=['POST'])
def settings():
    return render_template("settings.html")


@app.route('/me', methods=['POST'])
def me():
    return render_template("me.html")
