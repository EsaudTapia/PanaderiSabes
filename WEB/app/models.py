from email.policy import default
from flask_security import UserMixin, RoleMixin
from . import db


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
    active = db.Column(db.Boolean)
    fechaRegistro = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
    
    
class Role(db.Model):
    """User acount modal we"""

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    estatus = db.Column(db.Boolean)
    
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
    
    
class Insumo(db.Model):
    """Insumo table"""
    
    __tablename__ = 'insumos'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    cantidad = db.Column(db.Float)
    precio_compra = db.Column(db.Float)
    unidad_medida = db.Column(db.String(10))
    estatus = db.Column(db.Boolean)

    
    def __str__(self,name,description,cantidad,precio_compra,unidad_medida,estatus):
        self.name=name
        self.description=description
        self.cantidad=cantidad
        self.precio_compra=precio_compra
        self.unidad_medida=unidad_medida
        self.estatus=estatus
    
     # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)
    
class Receta(db.Model):
    """Insumo table"""
    
    __tablename__ = 'receta'
    
    id_r = db.Column(db.Integer, primary_key=True)
    id_pr = db.Column(db.Integer)
    id_in = db.Column(db.Integer)
    cantidadR = db.Column(db.Float)
    unidad = db.Column(db.String(10))

class Merma(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'merma'
    
    id = db.Column(db.Integer, primary_key=True)
    id_pr=db.Column(db.Integer, nullable=False)
    cantidad=db.Column(db.Integer, nullable=False)
    descripcion=db.Column(db.String(200), nullable=False)
    fechaRegistro=db.Column(db.DateTime)
    
class compra(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'compra'
    
    id = db.Column(db.Integer, primary_key=True)
    id_em = db.Column(db.Integer, nullable=False)
    id_provee = db.Column(db.Integer, nullable=False)    
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    fechaRegistro = db.Column(db.DateTime)
    
class DetalleCompra(db.Model):
    __tablename__ = 'detalle_compra'
    
    id = db.Column(db.Integer,primary_key=True)
    id_compra = db.Column(db.Integer, nullable=False)
    id_in = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    