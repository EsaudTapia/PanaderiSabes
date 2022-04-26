from multiprocessing import context
from flask import render_template,session,redirect,flash,url_for,request
from app.insumos.forms import Registro,Editar,Buscar
from . import insumos
from ..models import Insumo
from .. import db
from flask_security import login_required,roles_required ,current_user,roles_accepted

@insumos.route("/Listado")
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def listai():
    insumo_form = Registro()
    insumos= Insumo.query.all()
    inbus = Buscar()
    context= {
        'insumo_form': insumo_form,
        'insumos':insumos,
        'buscar_form': inbus
    }
    return render_template("insumos.html",**context)


@insumos.route('/listado',methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def buscar():
    buscar_form= Buscar()
    ins_form = Registro()
    ins=[]
    if buscar_form.validate_on_submit():
        ins = Insumo.query.filter_by(name=buscar_form.buscarNom.data)    
    context = {
            'insumo_form': ins_form,
            'insumos': ins,
            'buscar_form':buscar_form
        }
    
    return render_template("insumos.html", **context)


@insumos.route("/registro",methods=['GET','POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def registro():
    insumo_form = Registro()
    context = {
        'insumo_form': insumo_form
    }
    if request.method == 'POST':   
        nombre = str(request.form.get('name').upper())       
        descripcion = request.form.get('description')  
        unidad=request.form.get('Unidad_medida')
       
        #Consultamos si existe un insumo ya registrado con el email.
        insumo = Insumo.query.filter_by(name=nombre).first()
        
        if insumo: #Si se encontró un insumo, redireccionamos de regreso a la página de registro
            flash('El Insumo ya existe',category='error')
            return redirect(url_for('insumos.listai'))
        
        newinsumo=Insumo(
        name=nombre, description=descripcion,unidad_medida=unidad,precio_compra=0,cantidad=0,estatus=1)
        db.session.add(newinsumo)
        db.session.commit()
        flash('El insumo se guardo correctamente',category='correcto')
        return redirect(url_for('insumos.listai')) 
    else:
        flash('No se pudo realizar el registro de insumo',category='error' )      
        return redirect(url_for('insumos.listai'))  


@insumos.route('/update/<id>', methods=['POST','GET'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def updatein(id):
    if request.method == 'POST':
        insumo=Insumo.query.get(id)
        insumo.name = request.form.get('name') 
        insumo.description =  request.form.get('description')  
        insumo.unidad_medida=request.form.get('Unidad_medida')
        db.session.commit()
        flash('Producto actualizado')
        return redirect(url_for('insumos.listai'))
    else:
        insumo=Insumo.query.get(id)
        insumo_form_e = Editar()
        insumo_form_e.name.data=insumo.name
        insumo_form_e.description.data=insumo.description     
        insumo_form_e.Unidad_medida.data=insumo.unidad_medida
        context={
            'insumo_form_e': insumo_form_e,
            'insumos': insumo
        }
        return render_template('actualizarinsumo.html',**context)
    
@insumos.route('/delete/<id>', methods=['POST','GET'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def deletein(id):
    insumo=Insumo.query.get(id)
    insumo.estatus=0
    db.session.commit()
    flash('Producto Eliminado')
    return redirect(url_for('insumos.listai'))

@insumos.route('/activate/<id>', methods=['POST','GET'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def activatein(id):
    insumo=Insumo.query.get(id)
    insumo.estatus=1
    db.session.commit()
    flash('Producto Reactivado')
    return redirect(url_for('insumos.listai'))