from flask import Blueprint

examen =Blueprint('examen',__name__,url_prefix='/examen')

from . import views