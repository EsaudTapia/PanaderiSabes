from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import productos

@productos.route("/Listado",methods=['GET','POST'])
def listapr():
    return render_template("productos.html")
