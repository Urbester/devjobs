from devjobs import app
from flask import render_template


@app.route('/search', methods=['GET'])
def search():
    return render_template("search.html")
