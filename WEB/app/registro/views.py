from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import registro

@registro.route("/Registrate",methods=['GET','POST'])
def registrar():
    return render_template("registro.html")