from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import clientes

@clientes.route("/listadoclientes",methods=['GET','POST'])
def listac():
    return render_template("clientes.html")