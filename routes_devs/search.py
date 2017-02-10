from devjobs import app
from flask import render_template


@app.route('/search', methods=['POST'])
def search():
    return render_template("devs/search.html")
