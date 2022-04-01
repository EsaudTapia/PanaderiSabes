from flask import render_template,session,redirect,flash,url_for
from .forms import Registro, Editar
from .models import Producto
from .models import db
from . import productos

@productos.route("/Listado",methods=['GET','POST'])
def listapr():
    
    pro_form = Registro()
    
    productos = Producto.query.all()
    context = {
        'pro_form':pro_form,
        'productos': productos
    }
    return render_template("productos.html",**context)

@productos.route("/registro", methods=['POST'])
def registro():
    pro_form = Registro()
    nombre = pro_form.nombre.data.upper()
    
    u = Producto.query.filter_by(nombre = nombre).first()
    
    if u:
        
        flash("El producto ya existe.")
        return redirect(url_for('productos.listapr'))
    
    descripcion = pro_form.descripcion.data
    precioVenta = pro_form.precio.data
    
    new = Producto(nombre=nombre,precioVenta=precioVenta,descripcion=descripcion,status=1)
    db.session.add(new)
    db.session.commit()
    flash("El producto se ha registrado")
    return redirect(url_for('productos.listapr'))

@productos.route("/editar/<id>")
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
def update_post(id):
    pro_form = Editar()
    
    p = Producto.query.filter_by(id=id).first()
    
        
    p.nombre = pro_form.nombre.data.upper()
    p.precioVenta = pro_form.precio.data
    p.descripcion = pro_form.descripcion.data
        
        
    db.session.commit()
    flash("El producto se ha modificado.", category='correcto')
    
    return redirect(url_for('productos.listapr'))


@productos.route('/delete/<id>')
def delete(id):
    
    p=Producto.query.filter_by(id=id).first()
    p.status = 0
    db.session.commit()    
    flash('Se elimino correctamente', category='correcto')
    return redirect(url_for('productos.listapr'))

@productos.route('/active/<id>')
def active(id):
    
    p=Producto.query.filter_by(id=id).first()
    p.status = 1
    db.session.commit()    
    flash('Se activó correctamente', category='correcto')
    return redirect(url_for('productos.listapr'))