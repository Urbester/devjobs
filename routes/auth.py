from devjobs import app
from flask import render_template


@app.route('/login', methods=['POST'])
def login():
    return render_template("search.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/logout', methods=['POST'])
def logout():
    return render_template("index.html")
