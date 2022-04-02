from flask import render_template,session,redirect,flash,url_for
from  .forms import Registro
from . import clientes
from ..models import User,Role
from .. import db
from flask_security import login_required,roles_required ,current_user
from werkzeug.security import generate_password_hash

"""@clientes.route("/listadoclientes",methods=['GET','POST'])
def listac():
    return render_template("clientes.html")"""

@clientes.route("/registrocliente",methods=['GET','POST'])
@login_required
@roles_required('ADMINISTRADOR')
def registroc():
    cl_form = Registro()
    context={
        'cl_form': cl_form
    }
    if cl_form.validate_on_submit():
        nombre = cl_form.nombre.data
        apaterno = cl_form.apaterno.data
        amaterno = cl_form.amaterno.data
        numero = cl_form.numero.data
        calle = cl_form.calle.data
        colonia = cl_form.colonia.data
        cp = cl_form.cp.data
        telefono = cl_form.telefono.data
        email = cl_form.email.data
        password = cl_form.password.data
        e = User.query.filter_by(email=email).first()
        if e:
            flash("El cliente con correo {} ya existe.".format(email), category='error')
            return redirect(url_for('clientes.registroc'))
        new = User(nombre = nombre,
        apaterno = apaterno,
        amaterno = amaterno,
        numero = numero,
        calle = calle,
        colonia = colonia,
        cp = cp,
        telefono = telefono,
        email = email,
        password=generate_password_hash(password,method='sha256'),
        status = 1)
        default_role = Role.query.filter_by(id=3).first()
        new.roles.append(default_role)
        db.session.add(new)
        db.session.commit()
        flash("Se ha registrado.", category='correcto')
        
        return redirect(url_for('clientes.registroc'))
    return render_template('clientes.html',**context)