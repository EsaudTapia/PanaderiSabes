from flask import Blueprint

registro =Blueprint('registro',__name__,url_prefix='/registro')

from . import views