from flask import render_template,session,redirect,flash,url_for
from .forms import Registro
from ..models import Merma,Producto
from datetime import datetime
from . import mermas
from flask_security import login_required,roles_required ,current_user,roles_accepted
from .. import db

@mermas.route("/Listado",methods=['GET','POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def listam():
    
    me_form = Registro()
    
    mermas = Merma.query.join(Producto, Producto.id==Merma.id_pr).add_columns(Producto.nombre,Producto.id,Merma.cantidad,Merma.descripcion,Merma.fechaRegistro)
    
    productos = Producto.query.all()
    
    for p in productos:
        if p.status:
            me_form.producto.choices.append((p.id,p.nombre))
    
    context = {
        'me_form':me_form,
        'mermas':mermas
    }
    return render_template("mermas.html",**context)

@mermas.route("/listam_post",methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def listam_post():
    
    me_form = Registro()
    idpr = me_form.producto.data
    cantidad = me_form.cantidad.data
    des = me_form.descripcion.data
    hoy = datetime.today()
    
    prd = Producto.query.filter_by(id=idpr).first()
    
    if prd.cantidadPr - cantidad >= 0:
        prd.cantidadPr = prd.cantidadPr - cantidad
        new = Merma(id_pr=idpr,cantidad=cantidad,descripcion=des,fechaRegistro=hoy)
        db.session.add(new)
        
        db.session.commit()
        flash("La merma se ha registrado.", category="correcto")
    else:
        flash("El producto no cuenta con la cantidad suficiente.", category="error")
    return redirect(url_for("mermas.listam"))
