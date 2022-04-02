from flask import render_template,session,redirect,flash,url_for
from .forms import Registro, Editar
from ..models import User,Role
from . import empleados
from .. import db
from werkzeug.security import generate_password_hash
from flask_security import login_required,roles_required ,current_user

@empleados.route("/listado",methods=['GET','POST'])
@login_required
@roles_required('ADMINISTRADOR')
def listae():
    
    emp_form = Registro()
    roles= Role.query.all()
    roleAdmin = Role.query.get(1)
    roleEmp = Role.query.get(2)
    if roleAdmin == None or roleEmp==None:
         return render_template("empleados.html",roles=False)
    else:
    
     empleadosAdmin= roleAdmin.users
     empleados = roleEmp.users
     for r in roles:
         if r.name != "CLIENTE":
            emp_form.comboRol.choices.append((r.id,r.name))
     context = {
        'emp_form':emp_form,
        'empleados':empleados,
        'empleadosAdmin':empleadosAdmin
     }
     return render_template("empleados.html",**context)


@empleados.route("/registro",methods=['POST'])
@login_required
@roles_required('ADMINISTRADOR')
def registro():
    emp_form = Registro()
    nombre = emp_form.nombre.data.upper()
    apaterno = emp_form.apaterno.data.upper()
    amaterno = emp_form.amaterno.data.upper()
    numero = emp_form.numero.data
    calle = emp_form.calle.data
    colonia = emp_form.colonia.data
    cp = emp_form.cp.data
    telefono = emp_form.telefono.data
    email = emp_form.email.data
    password = emp_form.password.data
    comboRol= emp_form.comboRol.data
    e = User.query.filter_by(email=email).first()
    if e:
        flash("El empleado con correo {} ya existe.".format(email), category='error')
        return redirect(url_for('empleados.listae'))
    
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
    status = 1,
    active=1)
    default_role = Role.query.filter_by(id=comboRol).first()
    new.roles.append(default_role)
    db.session.add(new)
    db.session.commit()
    flash("El empleado se ha registrado.", category='correcto')
    
    return redirect(url_for('empleados.listae'))

@empleados.route("/editar/<id>")
@login_required
@roles_required('ADMINISTRADOR')
def update(id):
    emp_form = Editar()
    
    u = User.query.filter_by(id=id).first()
    
    roles = Role.query.all()
    ro = u.roles
    for r in ro:
        emp_form.comboRol.choices.append((r.id,r.name))
    for r in roles:
        
        if r.name != "CLIENTE":
            emp_form.comboRol.choices.append((r.id,r.name))
    
    emp_form.nombre.data = u.nombre
    emp_form.apaterno.data = u.apaterno
    emp_form.amaterno.data = u.amaterno
    emp_form.calle.data = u.calle
    emp_form.numero.data = u.numero
    emp_form.colonia.data = u.colonia
    emp_form.cp.data = u.cp
    emp_form.telefono.data = u.telefono
    emp_form.email.data = u.email
    
    context = {
        'emp_form': emp_form,
        'u':u
    }
    
    return render_template("editarEmpleado.html", **context)

@empleados.route("/editar/<id>", methods=['POST'])
@login_required
@roles_required('ADMINISTRADOR')
def update_post(id):
    pro_form = Editar()
    
    us = User.query.filter_by(id=id).first()
    r = us.roles
    roldel = Role.query.filter_by(id=r[0].id).first()
    us.roles.remove(roldel)
    db.session.commit()
    
    u = User.query.filter_by(id=id).first()
    
        
    u.nombre = pro_form.nombre.data.upper()
    u.apaterno = pro_form.apaterno.data.upper()
    u.amaterno = pro_form.amaterno.data.upper()
    u.calle = pro_form.calle.data
    u.numero = pro_form.numero.data
    u.colonia = pro_form.colonia.data
    u.cp = pro_form.cp.data
    u.telefono = pro_form.telefono.data
    u.email = pro_form.email.data
        
        
    default_role = Role.query.filter_by(id=pro_form.comboRol.data).first()
    u.roles.append(default_role)
    db.session.commit()
    flash("El empleado se ha modificado.", category='correcto')
    
    return redirect(url_for('empleados.listae'))

@empleados.route('/delete/<id>')
@login_required
@roles_required('ADMINISTRADOR')
def delete(id):
    
    u=User.query.filter_by(id=id).first()
    u.active = 0
    db.session.commit()    
    flash('Se elimino correctamente')
    return redirect(url_for('empleados.listae'))

@empleados.route('/active/<id>')
@login_required
@roles_required('ADMINISTRADOR')
def active(id):
    
    u=User.query.filter_by(id=id).first()
    u.active = 1
    db.session.commit()    
    flash('Se activó correctamente')
    return redirect(url_for('empleados.listae'))
