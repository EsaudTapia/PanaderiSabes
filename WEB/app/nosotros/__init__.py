from flask import Blueprint

nosotros =Blueprint('nosotros',__name__,url_prefix='/nosotros')

from . import views