from secrets import choice
from wtforms import Form,IntegerField,StringField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired
class Registro(FlaskForm):    
    emailLogin=EmailField('Email', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=35, message='Ingresa un año valido')])
    passwordLogin=PasswordField('Contrseña', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=100, message='Ingresa un año valido')])
   
   
    btnLogear = SubmitField("Entrar")