from flask import Blueprint

insumos =Blueprint('insumos',__name__,url_prefix='/insumos')

from . import views