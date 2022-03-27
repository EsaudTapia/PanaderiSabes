from wtforms import Form,IntegerField,StringField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired

class Registro(FlaskForm):    
    nombre=StringField('nombre', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=15, message='Ingresa nombre valido')])
    apaterno=StringField('apaterno', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=15, message='Ingresa un apellido valido')])
    amaterno=StringField('amaterno', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=15, message='Ingresa un apellido valido')])
    grupo=StringField('grupo', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=15, message='Ingresa un grupo valido')])
    matricula=StringField('Matricula', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=5, max=15, message='Ingresa una matricula valida')])
    sexo = RadioField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    dia=StringField('dia', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=2, message='Ingresa un dia valido')])
    mes=StringField('mes', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=2, message='Ingresa un mes valido')])
    año=StringField('año', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=4, max=4, message='Ingresa un año valido')])
    submit = SubmitField("Enviar")