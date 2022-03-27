from flask import Flask, redirect,render_template,url_for
from flask_wtf.csrf import CSRFProtect
from flask import request
from flask import make_response
from flask import flash
from flask import g
from app import create_app


import app.forms as forms

app=create_app()


csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


@app.route("/")
def index():
    return redirect(url_for('login.iniciar'))

if __name__=='__main__':
    csrf.init_app(app)
    app.run(port=3000)