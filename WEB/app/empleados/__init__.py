from flask import Blueprint

empleados =Blueprint('empleados',__name__,url_prefix='/empleados')

from . import views