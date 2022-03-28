from wtforms import Form,IntegerField,StringField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired

class Registro(FlaskForm):    
    name=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=50, message='Ingresa nombre valido')])
    description=StringField('Descripción', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=50, message='Ingresa una descripción valida')])
    submit = SubmitField("Guardar")