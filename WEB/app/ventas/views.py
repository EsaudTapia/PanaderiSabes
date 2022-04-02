from flask import render_template,session,redirect,flash,url_for
from flask_security import login_required,roles_required ,current_user
from ..models import User,Venta, DetalleVenta, Producto
from .. import db
from . import ventas

@ventas.route("/Listado",methods=['GET'])
@login_required
def listav():
    ventas = Venta.query.join(User, Venta.id_cl==User.id).add_columns(Venta.status,Venta.id, User.nombre,Venta.fechaRegistro,Venta.total)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("ventas.html",**context)

@ventas.route("/detalleventa/<id>",methods=['GET'])
@login_required
def detalle(id):
    ventas = Venta.query.join(DetalleVenta, DetalleVenta.id_venta==Venta.id).join(Producto, DetalleVenta.id_pr==Producto.id).add_columns(DetalleVenta.precio,DetalleVenta.total,DetalleVenta.cantidad,Producto.nombre).filter(Venta.id==id)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("detalles.html",**context)




@ventas.route("/ventaactive/<id>",methods=['GET'])
@login_required
def ventaact(id):
    ventas = Venta.query.join(DetalleVenta, DetalleVenta.id_venta==Venta.id).join(Producto, DetalleVenta.id_pr==Producto.id).add_columns(DetalleVenta.id_pr,DetalleVenta.cantidad).filter(Venta.id==id)

    for i in ventas:
        p = Producto.query.filter_by(id=i.id_pr).first()
        p.cantidadPr = p.cantidadPr - i.cantidad
        
        if p.cantidadPr < 0:
            flash("El producto {} no cuenta con la cantidad suficiente.".format(p.nombre), category="error")
            return redirect(url_for('ventas.listav'))
    
    ven = Venta.query.filter_by(id=id).first()    
    ven.status = "Realizada"
    
    db.session.commit()
    flash("La venta se ha realizado.", category="correcto")
    return redirect(url_for('ventas.listav'))

@ventas.route("/ventadelete/<id>",methods=['GET'])
@login_required
def ventadel(id):
    
    venta = Venta.query.filter_by(id=id).first()

    venta.status = "Cancelada"
    db.session.commit()
    flash("La venta se ha cancelado.", category="correcto")
    return redirect(url_for('ventas.listav'))


@ventas.route("/ListadoVentas",methods=['GET'])
@login_required
def listavcl():
    ventas = Venta.query.join(User, Venta.id_cl==User.id).add_columns(Venta.status,Venta.id, User.nombre,Venta.fechaRegistro,Venta.total).filter(Venta.id_cl==5)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("cliente-ventas.html",**context)

@ventas.route("/ventadeletecl/<id>",methods=['GET'])
@login_required
def ventadelcl(id):
    
    venta = Venta.query.filter_by(id=id).first()

    venta.status = "Cancelada"
    db.session.commit()
    flash("La venta se ha cancelado.", category="correcto")
    return redirect(url_for('ventas.listav'))

@ventas.route("/detalles/<id>",methods=['GET'])
@login_required
def detallecl(id):
    ventas = Venta.query.join(DetalleVenta, DetalleVenta.id_venta==Venta.id).join(Producto, DetalleVenta.id_pr==Producto.id).add_columns(DetalleVenta.precio,DetalleVenta.total,DetalleVenta.cantidad,Producto.nombre).filter(Venta.id==id)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("detalles.html",**context)