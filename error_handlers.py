from flask import render_template

from devjobs import app


@app.errorhandler(404)
def page_not_found_404(e):
    return render_template('ops.html'), 404


@app.errorhandler(500)
def page_not_found_500(e):
    return render_template('ops.html'), 500


@app.errorhandler(400)
def page_not_found_400(e):
    return render_template('ops.html'), 400