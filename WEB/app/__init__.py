import imp
from .config import DevelopmentConfig
import os
from flask import  Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

db = SQLAlchemy()


from .models import User
from .models import Role

userData = SQLAlchemyUserDatastore(db,User,Role)

def create_app():
    app=Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    
    @app.before_first_request
    def create_all():
        db.create_all()
    from .login.forms import Registro
    @app.route('/login')
    def login():
        form_login = Registro()
        context={
            'form_login':form_login
        }
        return render_template("login.html",**context)
        
    security = Security(app, userData)
    
    
    from .login import login
    from .clientes import clientes
    from .compras import compras
    from .empleados import empleados
    from .insumos import insumos
    from .mermas import mermas
    from .pedidos import pedidos
    from .productos import productos
    from .proveedores import proveedores
    from .roles import roles
    from .ventas import ventas
    from .registro import registro
    from .nosotros import nosotros
    from .inicio import inicio
    
    app.register_blueprint(login)
    app.register_blueprint(clientes)
    app.register_blueprint(compras)
    app.register_blueprint(empleados)
    app.register_blueprint(insumos)
    app.register_blueprint(mermas)
    app.register_blueprint(pedidos)
    app.register_blueprint(productos)
    app.register_blueprint(proveedores)
    app.register_blueprint(roles)
    app.register_blueprint(ventas)
    app.register_blueprint(registro)
    app.register_blueprint(nosotros)
    app.register_blueprint(inicio)
    
    return app
    