from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import mermas

@mermas.route("/Listado",methods=['GET','POST'])
def listam():
    return render_template("mermas.html")
