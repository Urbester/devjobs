from devjobs import app
from flask import render_template


@app.route('/settings', methods=['POST'])
def settings():
    return render_template("devs/settings.html")


@app.route('/dashboard', methods=['POST'])
def dashboard():
    return render_template("devs/dashboard.html")
