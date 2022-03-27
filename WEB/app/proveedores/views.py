from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import proveedores

@proveedores.route("/Listado",methods=['GET','POST'])
def listapro():
    return render_template("proveedores.html")
