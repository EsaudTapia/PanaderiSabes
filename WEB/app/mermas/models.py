from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Producto(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'producto'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precioVenta = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255))
    cantidadPr = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean)
    fechaRegistro = db.Column(db.DateTime)

class Merma(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'merma'
    
    id = db.Column(db.Integer, primary_key=True)
    id_pr=db.Column(db.Integer, nullable=False)
    cantidad=db.Column(db.Integer, nullable=False)
    descripcion=db.Column(db.String(200), nullable=False)
    fechaRegistro=db.Column(db.DateTime)
    