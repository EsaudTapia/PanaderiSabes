from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import roles

@roles.route("/Listado",methods=['GET','POST'])
def listarol():
    return render_template("roles.html")
