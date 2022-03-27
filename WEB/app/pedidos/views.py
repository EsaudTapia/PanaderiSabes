from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import pedidos

@pedidos.route("/Listado",methods=['GET','POST'])
def listape():
    return render_template("pedidos.html")
