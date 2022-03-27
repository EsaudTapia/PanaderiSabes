from flask import Flask

from app import examen
from .config import DevelopmentConfig
from .site import site
from .login import login
from .clientes import clientes
from .compras import compras
from .empleados import empleados

def create_app():
    app=Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(site)
    app.register_blueprint(login)
    app.register_blueprint(clientes)
    app.register_blueprint(compras)
    app.register_blueprint(empleados)
    return app