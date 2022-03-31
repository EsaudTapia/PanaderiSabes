from gettext import NullTranslations
from flask import render_template,session,redirect,flash,url_for
from numpy import False_
from app.forms import Registro
from ..empleados.models import Role,User,db
from . import registro

@registro.route("/Registrate",methods=['GET','POST'])
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
def delete(id):
    
    u=User.query.filter_by(id=id).first()
    u.status = 0
    db.session.commit()    
    flash('Se elimino correctamente')
    return redirect(url_for('registro.registrar'))

@registro.route('/active/<id>')
def active(id):
    
    u=User.query.filter_by(id=id).first()
    u.status = 1
    db.session.commit()    
    flash('Se activó correctamente')
    return redirect(url_for('registro.registrar'))
