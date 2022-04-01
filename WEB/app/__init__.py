import imp
from flask import Flask

from .config import DevelopmentConfig
from .site import site
from .login import login
from .clientes import clientes
from .compras import compras

import os
from flask import  Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

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



from .roles.models import db


from .empleados.models import User
from .roles.models import Role

userData = SQLAlchemyUserDatastore(db,User,Role)
from .proveedores.models import db
from .insumos.models import db
from .empleados.models import db 
from .productos.models import db 
def create_app():
    app=Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    
    @app.before_first_request
    def create_all():
        db.create_all()
        
        
    security = Security(app, userData)
    
    
    app.register_blueprint(site)
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