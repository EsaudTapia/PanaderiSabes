from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import empleados

@empleados.route("/listado",methods=['GET','POST'])
def listae():
    return render_template("empleados.html")
