from random import choices
from secrets import choice
from wtforms import Form,IntegerField,StringField,EmailField,SelectField,RadioField,SubmitField,validators, FloatField
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired


class Registro(FlaskForm):    
    nombre=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa nombre valido')])
    descripcion=StringField('Descripción', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=200, message='Ingresa un apellido valido')])
    precio=FloatField('Precio a la venta', [validators.DataRequired(message='El campo es requerido')])

    enviar = SubmitField("Enviar")
    
class Editar(FlaskForm):    
    nombre=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa nombre valido')])
    descripcion=StringField('Descripción', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=200, message='Ingresa un apellido valido')])
    precio=FloatField('Precio a la venta', [validators.DataRequired(message='El campo es requerido')])

    enviar = SubmitField("Enviar")
    
class Producir(FlaskForm):    
    
    cantidad=FloatField('Cantidad a producir', [validators.DataRequired(message='El campo es requerido')])

    enviar = SubmitField("Enviar")
    

class InsumosAdd(FlaskForm):    
    
    insumos=SelectField('Insumo', choices=[])
    
    cantidad=FloatField('Cantidad', [validators.DataRequired(message='El campo es requerido')])
    
    unidad=SelectField('Unidad', choices=[('Gm','Gramo'),('Kg','Kilogramos'),('Lt','Litro'),('Ml','Mililitro'),('Pz','Pieza')])

    enviar = SubmitField("Enviar")