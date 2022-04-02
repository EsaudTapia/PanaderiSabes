from email.policy import default
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()


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

    
