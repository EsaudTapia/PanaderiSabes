from flask import Blueprint

mermas =Blueprint('mermas',__name__,url_prefix='/mermas')

from . import views