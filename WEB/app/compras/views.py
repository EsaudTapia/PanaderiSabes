from flask import render_template,session,redirect,flash,url_for
from . import compras
from .forms import RegistroCompra

@compras.route("/Listado",methods=['GET','POST'])
def listaco():
    formcom= RegistroCompra()
    context = {
        'formcom':formcom,
       
     }
    
    return render_template("compras.html",**context)
