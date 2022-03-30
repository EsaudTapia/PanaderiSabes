from operator import or_
from flask import render_template,session,redirect,flash,url_for
from .form import Registro
from .form import Editar
from .form import Buscar
from . import proveedores
from .models import Proveedor
from .models import db



@proveedores.route("/Listado")
def listapro():
    
    pro_form = Registro()
    pr = Proveedor.query.all()
    buscar_form= Buscar()
    context = {
        'pro_form': pro_form,
        'proveedores': pr,
        'buscar_form':buscar_form
    }
    return render_template("proveedores.html", **context)


@proveedores.route('/listado',methods=['POST'])
def buscar():
    buscar_form= Buscar()
    pro_form = Registro()
    pr=[]
    if buscar_form.validate_on_submit():
        pr = Proveedor.query.filter_by(rfc=buscar_form.buscarRfc.data)
    
    context = {
            'pro_form': pro_form,
            'proveedores': pr,
            'buscar_form':buscar_form
        }
    
    return render_template("proveedores.html", **context)


@proveedores.route("/Listado_post", methods=["POST"])
def registro():
    pro_form = Registro()
    
    rfc = pro_form.rfc.data.upper()
    razon = pro_form.razon.data
    calle = pro_form.calle.data
    numero = pro_form.numero.data
    colonia = pro_form.colonia.data
    cp = pro_form.cp.data
    telefono = pro_form.telefono.data
    email = pro_form.email.data
    
    pr = Proveedor.query.filter_by(rfc=rfc).first()
    
    if pr:
        flash("El proveedor con RFC {} ya existe.".format( pro_form.rfc.data), category='error')
        return redirect(url_for('proveedores.listapro'))
    
    prc = Proveedor.query.filter_by(email=email).first()
    
    if prc:
        flash("El proveedor con correo {} ya existe.".format( pro_form.email.data), category='error')
        return redirect(url_for('proveedores.listapro'))
        
    new = Proveedor(rfc=rfc,razon=razon,calle=calle,numero=numero,colonia=colonia,cp=cp,telefono=telefono,email=email,active=1)
    
    db.session.add(new)
    
    db.session.commit()
    flash("El proveedor se ha registrado.", category='correcto')
    
    return redirect(url_for('proveedores.listapro'))

@proveedores.route("/editar/<id>")
def update(id):
    pro_form = Editar()
    
    pr = Proveedor.query.filter_by(id=id).first()
    
    pro_form.rfc.data = pr.rfc
    pro_form.razon.data = pr.razon
    pro_form.calle.data = pr.calle
    pro_form.numero.data = pr.numero
    pro_form.colonia.data = pr.colonia
    pro_form.cp.data = pr.cp
    pro_form.telefono.data = pr.telefono
    pro_form.email.data = pr.email
    
    context = {
        'pro_form': pro_form,
        'pr':pr
    }
    
    return render_template("editarProveedor.html", **context)

@proveedores.route("/editar/<id>", methods=['POST'])
def update_post(id):
    pro_form = Editar()
    
    pr = Proveedor.query.filter_by(id=id).first()
    
    if pro_form.validate_on_submit():
        
        pr.rfc = pro_form.rfc.data.upper()
        pr.razon = pro_form.razon.data
        pr.calle = pro_form.calle.data
        pr.numero = pro_form.numero.data
        pr.colonia = pro_form.colonia.data
        pr.cp = pro_form.cp.data
        pr.telefono = pro_form.telefono.data
        pr.email = pro_form.email.data
        
        db.session.commit()
        flash("El proveedor se ha modificado.", category='correcto')
    
    return redirect(url_for('proveedores.listapro'))

@proveedores.route('/delete/<id>')
def delete(id):
    
    pr=Proveedor.query.filter_by(id=id).first()
    pr.active = 0
    db.session.commit()    
    flash('Se elimino correctamente')
    return redirect(url_for('proveedores.listapro'))

@proveedores.route('/active/<id>')
def active(id):
    
    pr=Proveedor.query.filter_by(id=id).first()
    pr.active = 1
    db.session.commit()    
    flash('Se activó correctamente')
    return redirect(url_for('proveedores.listapro'))

