from flask import render_template,session,redirect,flash,url_for
from app.roles.forms import Registro
from . import roles

@roles.route("/Listado",methods=['GET','POST'])
def listarol():
    role_form = Registro()
    context = {
        'role_form': role_form
    }
    return render_template("roles.html", **context)
