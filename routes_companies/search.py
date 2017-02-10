from devjobs import app
from flask import render_template


@app.route('/c/search', methods=['GET'])
def c_search():
    return render_template("companies/dashboard.html")
