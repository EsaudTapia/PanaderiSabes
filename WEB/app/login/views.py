from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import login

@login.route("/iniciar",methods=['GET','POST'])
def iniciar():
    return render_template("login.html")
