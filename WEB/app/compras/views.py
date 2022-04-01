from flask import render_template,session,redirect,flash,url_for
from ..proveedores.models import Proveedor
from ..insumos.models import Insumo
from . import compras
from .forms import RegistroCompra

@compras.route("/listado",methods=['GET','POST'])
def listaco():
    formcom= RegistroCompra()
    proveedores = Proveedor.query.all()
    insumos = Insumo.query.all()
   
    context = {
        'formcom':formcom,
        'proveedores': proveedores,
        'insumos': insumos
     }
    
    return render_template("compras.html",**context)


@compras.route("/registrarCompra",methods=['GET','POST'])
def registrar():
    formcom= RegistroCompra()
   
   
    if formcom.validate_on_submit():
      flash("Seamorra.", category='correcto')
      return redirect(url_for('compras.listaco'))
  
  
    flash('no amarra',category='error')
    return redirect(url_for('compras.listaco'))
