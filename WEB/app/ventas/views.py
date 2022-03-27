from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import ventas

@ventas.route("/Listado",methods=['GET','POST'])
def listav():
    return render_template("ventas.html")
