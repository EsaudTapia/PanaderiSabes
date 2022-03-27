from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import compras

@compras.route("/Listado",methods=['GET','POST'])
def listaco():
    return render_template("compras.html")
