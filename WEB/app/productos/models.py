from email.policy import default
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()


class Producto(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'producto'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precioVenta = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255))
    status = db.Column(db.Boolean)
    fechaRegistro = db.Column(db.DateTime)