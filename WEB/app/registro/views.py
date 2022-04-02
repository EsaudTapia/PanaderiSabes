from gettext import NullTranslations
from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from ..models import Role,User
from .. import db
from . import registro
from flask_security import login_required,roles_required ,current_user

@registro.route("/Registrate",methods=['GET','POST'])
@login_required
def registrar():
     
    role_cliente = Role.query.get(3)
 
    if role_cliente == None:
         return render_template("registro.html",roles=False)
    else:    
    
     clientes= role_cliente.users
     context = {
         'clientes':clientes
     }
    return render_template("registro.html",**context)


@registro.route('/delete/<id>')
@login_required
def delete(id):
    
    u=User.query.filter_by(id=id).first()
    u.active = 0
    db.session.commit()    
    flash('Se elimino correctamente')
    return redirect(url_for('registro.registrar'))

@registro.route('/active/<id>')
@login_required
def active(id):
    
    u=User.query.filter_by(id=id).first()
    u.active = 1
    db.session.commit()    
    flash('Se activó correctamente')
    return redirect(url_for('registro.registrar'))
