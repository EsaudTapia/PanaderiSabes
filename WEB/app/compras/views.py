from datetime import datetime
from flask import render_template, request,session,redirect,flash,url_for
from sqlalchemy import desc
from ..proveedores.models import Proveedor
from ..insumos.models import Insumo
from . import compras
from .forms import AddCart, Addinsumo, RegistroCompra
from .models import Insumo
from .models import compra as comprasl
from .models import DetalleCompra
from .models import db

@compras.route("/listado",methods=['GET','POST'])
def listaco():
    formcom= RegistroCompra()
    d= Addinsumo()
    addcart= AddCart()
    proveedores = Proveedor.query.all()
    insumos = Insumo.query.all()
   
    context = {
        'formcom':formcom,
        'd':d,
        'f':addcart,
        'proveedores': proveedores,
        'insumos': insumos
     }
    
    return render_template("compras.html",**context)

lista = []



@compras.route("/insumoscart", methods=['POST'])
def cart():
    produ_form = AddCart()
    
    for i in lista:
        if i['id'] == request.form.get("insumo"):
            i['cantidad'] = int(i['cantidad'])  + int(request.form.get("cantidad"))
            i['total'] = float(i['precio'])*int(i['cantidad'])
            return redirect(url_for("compras.listaco"))
    
    
    insumos= Insumo.query.get(request.form.get("insumo"))   
    
          
    l = {
        'id':insumos.id,
        'nombre':insumos.name,
        'precio':request.form.get("precio"),
        'cantidad':request.form.get("cantidad"),        
        'total':float(request.form.get("precio"))*int(request.form.get("cantidad")),
        'proveedor':request.form.get("proveedor")
    }
    
    lista.append(l)
    
    print(lista)
    
    return redirect(url_for("compras.listacom"))


@compras.route("/insumos",methods=['GET'])
def listacom():
    proveedores = Proveedor.query.all()
    insumos = Insumo.query.all()
   
    formcom= RegistroCompra()
    produ_form = AddCart()
    v = Addinsumo()
    final = 0
    for i in lista:
        final+=float(i["total"])
    v.total.data = final
    context = {      
        'formcom':formcom,
        'lista':lista,
        'f':produ_form,
        'd':v,
        'final':final,
        'proveedores': proveedores,
        'insumos': insumos
    }
    return render_template("compras.html",**context)



@compras.route("/insumocompra", methods=['POST'])
def compra():
    d = Addinsumo()
    hoy = datetime.today()
    
    em=1
    
    compra = comprasl(id_em=em,id_provee=lista[0]['proveedor'],total=d.total.data,status="Realizado",fechaRegistro=hoy)
   
    db.session.add(compra)
    db.session.commit()
    
    ve = compra.query.all()
    id=0
    for idc in ve:
      id=idc.id
    
      
    print(id)
    
    for i in lista:
        ins= Insumo.query.get(i['id'])
        if ins.unidad_medida == 'Pz':
          ins.cantidad += i['cantidad']
          
        else:
            ins.cantidad += 1000*int(i['cantidad'])
        
        d = DetalleCompra(id_compra=id,id_in=i['id'],precio=i['precio'],cantidad=i['cantidad'],total=i['total'])
        db.session.add(d)
    
    db.session.commit()
    lista.clear()
    return redirect(url_for("compras.listacom"))