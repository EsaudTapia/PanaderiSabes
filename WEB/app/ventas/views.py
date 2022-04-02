from flask import render_template,session,redirect,flash,url_for

from .models import User,Role
from . models import Venta, DetalleVenta, Producto
from . models import db
from . import ventas

@ventas.route("/Listado",methods=['GET'])
def listav():
    ventas = Venta.query.join(User, Venta.id_cl==User.id).add_columns(Venta.status,Venta.id, User.nombre,Venta.fechaRegistro,Venta.total)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("ventas.html",**context)


@ventas.route("/detalleventa/<id>",methods=['GET'])
def detalle(id):
    ventas = Venta.query.join(DetalleVenta, DetalleVenta.id_venta==Venta.id).join(Producto, DetalleVenta.id_pr==Producto.id).add_columns(DetalleVenta.precio,DetalleVenta.total,DetalleVenta.cantidad,Producto.nombre).filter(Venta.id==id)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("detalles.html",**context)




@ventas.route("/ventaactive",methods=['GET'])
def ventaact():
    ventas = Venta.query.join(User, Venta.id_cl==User.id).add_columns(Venta.status,Venta.id, User.nombre,Venta.fechaRegistro,Venta.total)
    print(str(ventas))
    context = {
        'ventas': ventas
    }
    return render_template("ventas.html",**context)
