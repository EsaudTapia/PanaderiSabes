from flask import render_template, request,session,redirect,flash,url_for
from app.roles.forms import Registro
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from . import roles

from .models  import Role,db


@roles.route("/Listado",methods=['GET','POST'])
def listarol():
    role_form = Registro()
    roles = Role.query.all()
    context = {
        'role_form': role_form,
        'roles': roles
    }
    
    
    
      
        
    return render_template("roles.html", **context)



@roles.route("/registro",methods=['GET','POST'])
def registro():
    role_form = Registro()
    context = {
        'role_form': role_form
    }
    if role_form.validate_on_submit():    
       nombre = str(request.form.get('name').upper())
       
       descripcion = request.form.get('description')
       #Consultamos si existe un usuario ya registrado con el email.
       rol = Role.query.filter_by(name=nombre).first()
       
       if rol: #Si se encontró un usuario, redireccionamos de regreso a la página de registro
        flash('El Rol ya existe',category='error')
        return redirect(url_for('roles.listarol'))
       
       newRole=Role(
       name=nombre, description=descripcion)
       db.session.add(newRole)
       db.session.commit()
       flash('El rol se guardo correctamente',category='correcto')
       return redirect(url_for('roles.listarol'))        
    return render_template("roles.html", **context)
