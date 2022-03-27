from flask import Blueprint

pedidos =Blueprint('pedidos',__name__,url_prefix='/pedidos')

from . import views