from flask import render_template, request,session,redirect,flash,url_for
from app.roles.forms import Registro
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from . import roles

from .models  import Role,db


@roles.route("/Listado",methods=['GET','POST'])
def listarol():
    role_form = Registro()
    context = {
        'role_form': role_form
    }
      
        
    return render_template("roles.html", **context)



@roles.route("/registro",methods=['GET','POST'])
def registro():
    role_form = Registro()
    context = {
        'role_form': role_form
    }
    if role_form.validate_on_submit():    
       nombre = request.form.get('name')
       descripcion = request.form.get('description')
       newRole=Role(
       name=nombre, description=descripcion)
       db.session.add(newRole)
       db.session.commit()
       flash('amarro')
       return redirect(url_for('roles.listarol'))        
    return render_template("roles.html", **context)
