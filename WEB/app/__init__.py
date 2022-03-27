import imp
from flask import Flask

from .config import DevelopmentConfig
from .site import site
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

def create_app():
    app=Flask(__name__)
    app.config.from_object(DevelopmentConfig)
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
    return app