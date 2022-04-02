from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db= SQLAlchemy()

class Role(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    estatus = db.Column(db.Boolean)


users_roles = db.Table('users_roles', 
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                       )

#definimos la clase del usuario obo

class User(UserMixin, db.Model):
    """User acount modal we"""
    
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    amaterno = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(5), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    colonia = db.Column(db.String(50), nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean)
    fechaRegistro = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
    



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

class Venta(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'venta'
    
    id = db.Column(db.Integer, primary_key=True)
    id_em = db.Column(db.String(50), nullable=False)
    id_cl = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    fechaRegistro = db.Column(db.DateTime)
    
class DetalleVenta(db.Model):
    __tablename__ = 'detalle_venta'
    
    id = db.Column(db.Integer,primary_key=True)
    id_venta = db.Column(db.Integer, nullable=False)
    id_pr = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)