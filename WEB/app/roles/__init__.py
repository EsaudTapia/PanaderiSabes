from flask import Blueprint

roles =Blueprint('roles',__name__,url_prefix='/roles')

from . import views