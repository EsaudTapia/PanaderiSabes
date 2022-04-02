from flask import render_template, request,session,redirect,flash,url_for
from .forms import Editar
from app.roles.forms import Registro
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from . import roles
from flask_security import login_required,roles_required ,current_user
from ..models  import Role
from .. import db


@roles.route("/Listado",methods=['GET','POST'])
@login_required
def listarol():
    role_form = Registro()
    roles = Role.query.all()
    context = {
        'role_form': role_form,
        'roles': roles
    }
    return render_template("roles.html", **context)



@roles.route("/registro",methods=['GET','POST'])
@login_required
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
       name=nombre, description=descripcion,estatus=1)
       db.session.add(newRole)
       db.session.commit()
       flash('El rol se guardo correctamente',category='correcto')
       return redirect(url_for('roles.listarol'))        
    return render_template("roles.html", **context)


@roles.route('/delete/<id>')
@login_required
def delete(id):
    idrol=id
    rol=Role.query.get(id)
    rol.estatus = 0
    db.session.commit()    
    flash('se elimino correctamente')
    return redirect(url_for('roles.listarol'))

@roles.route('/activate/<id>')
@login_required
def activate(id):
    idrol=id
    rol=Role.query.get(id)
    rol.estatus = 1
    db.session.commit()    
    flash('se activo correctamente')
    return redirect(url_for('roles.listarol'))


@roles.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    rolesEdit= Role.query.get(id)
    role_form_e= Editar()
    role_form_e.name_e.data=rolesEdit.name
    role_form_e.description_e.data=rolesEdit.description
    context = {
        'role_form_e': role_form_e,
        'rolesEdit': rolesEdit
    }
    if request.method == 'POST':
        rolesEdit= Role.query.get(id)
        rolesEdit.name= request.form.get('name_e').upper()
        rolesEdit.description= request.form.get('description_e')
       # rolesEdit.description= role_form_e.description_e.data       
        print(request.form.get('name_e'))
        print(request.form.get('description_e'))    
       
        db.session.commit()
       
        flash('El rol se actualizó correctamente {}'.format(id),category='correcto')
        return redirect(url_for('roles.listarol'))
    else:
        return render_template("editarRol.html", **context)