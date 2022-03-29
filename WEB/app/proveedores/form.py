from wtforms import Form,IntegerField,StringField,TextAreaField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired

class Registro(FlaskForm):    
    
    rfc=StringField('RFC', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=10, max=13, message='Ingresa nombre valido')])
    razon=StringField('Razon social', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=2, max=100, message='Ingresa nombre valido')])
    calle=StringField('Calle', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=2, max=50, message='Ingresa nombre valido')])
    numero=StringField('Numero exterior', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=6, message='Ingresa nombre valido')])
    colonia=StringField('Colonia', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa nombre valido')])
    cp=IntegerField('C.P.', [validators.DataRequired(message='El campo es requerido')])
    
    telefono=StringField('Telefono', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=10, max=10, message='Ingresa nombre valido')])
    email=EmailField('Email', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=2, max=50, message='Ingresa nombre valido')])
    submit = SubmitField("Guardar")