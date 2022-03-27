from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import insumos

@insumos.route("/Listado",methods=['GET','POST'])
def listai():
    return render_template("insumos.html")
