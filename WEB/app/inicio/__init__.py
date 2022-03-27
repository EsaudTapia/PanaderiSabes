from flask import Blueprint

inicio =Blueprint('inicio',__name__,url_prefix='/inicio')

from . import views