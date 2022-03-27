from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import inicio

@inicio.route("/",methods=['GET','POST'])
def inicio():
    return render_template("inicio.html")