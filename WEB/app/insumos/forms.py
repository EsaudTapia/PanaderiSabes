from ast import In
from wtforms import Form,IntegerField,StringField,TextAreaField,EmailField,SelectField,RadioField,SubmitField,validators,DecimalField,FloatField
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired

class Registro(FlaskForm):    
    name=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=50, message='Ingresa nombre valido')])
    description=TextAreaField('Descripción', [validators.DataRequired(message='El campo es requerido')
                                                                                                     ])
    
    precio_compra=DecimalField('Precio de compra', [validators.DataRequired(message='El campo es requerido')
                                                                                                     ])
    Unidad_medida=SelectField('Unidad', choices=[("Pz.","Piezas"),("Lt","Litros"),("Kg","Kilos")])
    submit = SubmitField("Guardar")
    
class Editar(FlaskForm):    
    name=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=50, message='Ingresa nombre valido')])
    description=TextAreaField('Descripción', [validators.DataRequired(message='El campo es requerido')
                                                                                                     ])
    cantidad=IntegerField('Cantidad', [validators.DataRequired(message='El campo es requerido')
                                                                                                     ])
    precio_compra=FloatField('Precio de compra', [validators.DataRequired(message='El campo es requerido')
                                                                                                     ])
    Unidad_medida=SelectField('Unidad', choices=[("Pz.","Piezas"),("Lt","Litros"),("Kg","Kilos")])
    editar = SubmitField("Guardar")
class Buscar(FlaskForm):
    buscarNom= StringField('', [validators.length(min=2,max=19)])
    buscar= SubmitField('Buscar')
