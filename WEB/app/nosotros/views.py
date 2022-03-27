from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import nosotros

@nosotros.route("/info",methods=['GET','POST'])
def info():
    return render_template("nosotros.html")