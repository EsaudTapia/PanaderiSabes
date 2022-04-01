from wtforms import Form,IntegerField,StringField,TextAreaField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired

class Registro(FlaskForm):    
    
    producto=SelectField('Producto', choices=[])
    descripcion=StringField('Descripción', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=2, max=200, message='Ingresa nombre valido')])
    
    cantidad=IntegerField('Cantidad', [validators.DataRequired(message='El campo es requerido'),validators.number_range(min=1,message="Valor no valido.")])
    
    submit = SubmitField("Guardar")