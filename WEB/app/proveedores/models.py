from email.policy import default
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Proveedor(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'proveedor'
    
    id = db.Column(db.Integer, primary_key=True)
    rfc=db.Column(db.String(13), nullable=False)
    razon=db.Column(db.String(100), nullable=False)
    calle=db.Column(db.String(50), nullable=False)
    numero=db.Column(db.String(6), nullable=False)
    colonia=db.Column(db.String(50), nullable=False)
    cp=db.Column(db.Integer, nullable=False)
    
    telefono=db.Column(db.String(10), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    active=db.Column(db.Boolean, nullable=False)
    fechaRegistro=db.Column(db.DateTime)
    