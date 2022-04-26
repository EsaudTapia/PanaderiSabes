import os
from wsgiref import validate
from werkzeug.utils import secure_filename
from flask import render_template,session,redirect,flash,url_for,request
from .forms import Registro, Editar, InsumosAdd, Producir, AddCart, AddVenta
from ..models import Producto,Insumo,Receta,Venta,DetalleVenta
from .. import db
from . import productos
from datetime import datetime
from flask_security import login_required,roles_required ,current_user,roles_accepted


@productos.route("/Listado",methods=['GET','POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def listapr():
    
    pro_form = Registro()
    prod_form = Producir()
    productos = Producto.query.all()
    context = {
        'pro_form':pro_form,
        'productos': productos,
        'prod_form':prod_form
    }
    return render_template("productos.html",**context)

lista = []

@productos.route("/productos",methods=['GET'])
@login_required
def listaprcl():
    
    productos = Producto.query.all()
    
    produ_form = AddCart()
    v = AddVenta()
    final = 0
    for i in lista:
        final+=float(i["total"])
    v.total.data = final
    context = {
        'productos': productos,
        'lista':lista,
        'f':produ_form,
        'd':v,
        'final':final
    }
    return render_template("productos-cliente.html",**context)

@productos.route("/productosventa", methods=['POST'])
@login_required
def venta():
    if lista == []:
        flash("El carrito esta vacio.", category="error")
        return redirect(url_for("productos.listaprcl"))
        
    d = AddVenta()
    hoy = datetime.today()
    
    idcl = current_user.id
    
    venta = Venta(id_em=0,id_cl=idcl,total=d.total.data,status="pendiente",fechaRegistro=hoy)
    
    db.session.add(venta)
    db.session.commit()
    ve = Venta.query.filter_by(total=d.total.data,id_cl=idcl,status="pendiente").first()
    for i in lista:
        d = DetalleVenta(id_venta=ve.id,id_pr=i['id'],precio=i['precioVenta'],cantidad=i['cantidad'],total=i['total'])
        db.session.add(d)
    
    db.session.commit()
    lista.clear()
    return redirect(url_for("productos.listaprcl"))

@productos.route("/productoscart", methods=['POST'])
@login_required
def cart():
    produ_form = AddCart()
    
    for i in lista:
        if i['id'] == request.form.get("id"):
            i['cantidad'] = int(i['cantidad'])  + int(request.form.get("cantidad"))
            i['total'] = float(i['precioVenta'])*int(i['cantidad'])
            return redirect(url_for("productos.listaprcl"))
    l = {
        'id':request.form.get("id"),
        'nombre':request.form.get("nombre"),
        'precioVenta':request.form.get("precioVenta"),
        'cantidad':request.form.get("cantidad"),
        'total':float(request.form.get("precioVenta"))*int(request.form.get("cantidad"))
    }
    
    lista.append(l)
    
    return redirect(url_for("productos.listaprcl"))

@productos.route("/registro", methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def registro():
    pro_form = Registro()
    
    if pro_form.validate() == False:
        flash("No puedes ingresar cantidades negativas.",category="error")
        return redirect(url_for('productos.listapr'))
        
    nombre = pro_form.nombre.data.upper()
    
    u = Producto.query.filter_by(nombre = nombre).first()
    
    if u:
        
        flash("El producto ya existe.")
        return redirect(url_for('productos.listapr'))
    
    descripcion = pro_form.descripcion.data
    precioVenta = pro_form.precio.data
    
    new = Producto(nombre=nombre,precioVenta=precioVenta,descripcion=descripcion,cantidadPr=0,status=1)
    db.session.add(new)
    db.session.commit()
    p = Producto.query.filter_by(nombre=nombre,precioVenta=precioVenta,descripcion=descripcion).first()
    imagen = request.files['imagen']
    ext = imagen.filename
    ext = ext.split('.')
    if ext[1] == 'png' or ext[1] == 'jpeg' or ext[1] == 'jpg':
        img_name = secure_filename('img{}'.format(p.id))
        appp = 'app'
        ruta = os.path.abspath('.\{}\static\img\{}.{}'.format(appp,img_name,ext[1]))
        imagen.save(ruta)
        flash("El producto se ha registrado.")
    else:
         flash("La imagen no se ha registrado.")
         
    return redirect(url_for('productos.listapr'))

@productos.route("/editar/<id>")
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def update(id):
    pro_form = Editar()
    
    p = Producto.query.filter_by(id=id).first()
    
    pro_form.nombre.data = p.nombre
    pro_form.precio.data = p.precioVenta
    pro_form.descripcion.data = p.descripcion
    
    context = {
        'pro_form': pro_form,
        'p':p
    }
    
    return render_template("editarProducto.html", **context)

@productos.route("/editar/<id>", methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def update_post(id):
    pro_form = Editar()
    
    p = Producto.query.filter_by(id=id).first()
    
        
    p.nombre = pro_form.nombre.data.upper()
    p.precioVenta = pro_form.precio.data
    p.descripcion = pro_form.descripcion.data
    
        
    db.session.commit()
    if not request.files['imagen']:
        flash("El producto se ha modificado.", category='correcto')
        return redirect(url_for('productos.listapr'))
    
    imagen = request.files['imagen']
    ext = imagen.filename
    ext = ext.split('.')
    if ext[1] == 'jpg':
        img_name = secure_filename('img{}'.format(p.id))
        appp = 'app'
        ruta = os.path.abspath('.\{}\static\img\{}.{}'.format(appp,img_name,ext[1]))
        imagen.save(ruta)
        flash("El producto se ha registrado.")
    else:
         flash("La imagen no se ha registrado.")
    
    return redirect(url_for('productos.listapr'))


@productos.route('/delete/<id>')
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def delete(id):
    
    p=Producto.query.filter_by(id=id).first()
    p.status = 0
    db.session.commit()    
    flash('Se elimino correctamente', category='correcto')
    return redirect(url_for('productos.listapr'))

@productos.route('/active/<id>')
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def active(id):
    
    p=Producto.query.filter_by(id=id).first()
    p.status = 1
    db.session.commit()    
    flash('Se activó correctamente', category='correcto')
    return redirect(url_for('productos.listapr'))

@productos.route('/producto-insumo/<id>')
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def proin(id):
    
    insumo_form = InsumosAdd()
    
    p=Producto.query.filter_by(id=id).first()
    
    insumos = Insumo.query.join(Receta, Insumo.id==Receta.id_in).join(Producto, Receta.id_pr==Producto.id).add_columns(Receta.id_r,Receta.id_in,Insumo.id, Insumo.name, Receta.cantidadR, Receta.unidad ).filter(Producto.id == id)  
    print(str(insumos))
    ins = Insumo.query.all()
    
    
    for i in ins:
        
        insumo_form.insumos.choices.append((i.id,i.name))
    
    
    context = {
        'insumos':insumos,
        'insumo_form':insumo_form
    }
    
    return render_template("productos-insumos.html", **context)


@productos.route('/producto-insumo/<id>', methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def proin_post(id):
    
    insumo_form = InsumosAdd()
    
    ins = insumo_form.insumos.data
    pr = id
    cantidadR = insumo_form.cantidad.data
    unidad = insumo_form.unidad.data
    
    insumo = Insumo.query.filter_by(id=ins).first()
    
    if insumo.unidad_medida ==  "Kg":
        if unidad != "Gm" and unidad != "Kg":
            flash("Elije unidad Gramo o Kilogramo.", category="error")
            return redirect(url_for('productos.proin', id=id))
    if insumo.unidad_medida ==  "Lt":
        if unidad != "Ml" and unidad != "Lt":
            flash("Elije unidad Mililitro o Litro.", category="error")
            return redirect(url_for('productos.proin', id=id))
    if insumo.unidad_medida ==  "Pz":
        if unidad != "Pz":
            flash("Elije unidad Pieza.", category="error")
            return redirect(url_for('productos.proin', id=id))
    
    if unidad == "Pz":
        cantidadR =  int(cantidadR)
        
    receta = Receta.query.filter_by(id_pr=pr,id_in=ins).first()
    
    if receta:
        receta.cantidadR=cantidadR
        receta.unidad=unidad
    else:
        new = Receta(id_pr=pr,id_in=ins,cantidadR=cantidadR,unidad=unidad)
        db.session.add(new)
    
    
    db.session.commit()
    
    
    
    return redirect(url_for('productos.proin', id=id))

@productos.route('/delproducto-insumo/<id>')
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def borrar(id):

    re = Receta.query.filter_by(id_r=id).first()
    idp = re.id_pr
    db.session.delete(re)
    db.session.commit()
    
    return redirect(url_for('productos.proin', id=idp))



@productos.route('/producir/<id>')
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def producir(id):
    
    prod_form = Producir()
    
    context = {
        'prod_form':prod_form
    }
    return render_template("producto-producir.html", **context)

@productos.route('/producir/<id>', methods=['POST'])
@login_required
@roles_accepted('ADMINISTRADOR','EMPLEADO')
def producir_post(id):
    
    prod_form = Producir()
    cantidad = prod_form.cantidad.data
    insumos = Insumo.query.join(Receta, Insumo.id==Receta.id_in).join(Producto, Receta.id_pr==Producto.id).add_columns(Receta.id_r,Receta.id_in,Insumo.id, Insumo.name, Receta.cantidadR, Receta.unidad ).filter(Producto.id == id) 
    cont = 0
    for i in insumos:
        cont = cont + 1
        ins = Insumo.query.filter_by(id=i.id_in).first()
        
        if i.unidad == "Gm" or i.unidad == "Ml": 
            ins.cantidad = ins.cantidad - (i.cantidadR * cantidad)
        elif i.unidad == "Kg" or i.unidad == "Lt": 
            ins.cantidad = ins.cantidad - (i.cantidadR * cantidad * 1000)
        else:
            ins.cantidad = ins.cantidad - (i.cantidadR * int(cantidad))
        
        if ins.cantidad < 0:
            flash("Insumo {} insuficiente.".format(ins.name), category="error")
            return redirect(url_for('productos.listapr'))
    producto = Producto.query.filter_by(id=id).first()
    
    if cont > 0:
        producto.cantidadPr = producto.cantidadPr + cantidad
        db.session.commit()
    else:
        flash("El producto no tiene insumos", category="error")
        return redirect(url_for('productos.listapr'))
    return redirect(url_for('productos.listapr'))

