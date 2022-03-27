from flask import Blueprint

clientes =Blueprint('clientes',__name__,url_prefix='/clientes')

from . import views