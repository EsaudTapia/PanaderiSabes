from operator import or_
from flask import render_template,session,redirect,flash,url_for
from .form import Registro
from . import proveedores
from .models import Proveedor
from .models import db

@proveedores.route("/Listado")
def listapro():
    
    pro_form = Registro()
    pr = Proveedor.query.all()
    
    context = {
        'pro_form': pro_form,
        'proveedores': pr
    }
    return render_template("proveedores.html", **context)


@proveedores.route("/Listado_post", methods=["POST"])
def registro():
    pro_form = Registro()
    
    rfc = pro_form.rfc.data
    razon = pro_form.razon.data
    calle = pro_form.calle.data
    numero = pro_form.numero.data
    colonia = pro_form.colonia.data
    cp = pro_form.cp.data
    telefono = pro_form.telefono.data
    email = pro_form.email.data
    
    pr = Proveedor.query.filter(rfc=rfc,email=email).first()
    
    if pr:
        flash("El proveedor ya existe.", category='error')
        return redirect(url_for('proveedores.listapro'))
        
    new = Proveedor(rfc=rfc,razon=razon,calle=calle,numero=numero,colonia=colonia,cp=cp,telefono=telefono,email=email,active=1)
    
    db.session.add(new)
    
    db.session.commit()
    flash("El proveedor se ha registrado.", category='correcto')
    
    return redirect(url_for('proveedores.listapro'))

