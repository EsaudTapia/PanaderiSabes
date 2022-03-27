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
    
class Exform(FlaskForm):
    matricula = StringField('Matrícula', validators=[DataRequired()])
    grupo = StringField('Grupo', validators=[DataRequired()])
    pre1 = RadioField('¿Cual es la suma de 2 + 2?',choices=[('2','4'),('0','3'),('0','5'),('0','2')], validators=[DataRequired()])
    pre2 = RadioField('¿Cuál es la capital de Hungría?',choices=[('0','Viena'),('2','Budapest'),('0','Praga'),('0','Estambul')], validators=[DataRequired()])
    pre3 = RadioField('¿cuántos huesos tiene el cuerpo humano?',choices=[('0','208'),('0','306'),('0','15'),('2','206')], validators=[DataRequired()])
    pre4 = RadioField('¿Cuantos metros es un kilometro?',choices=[('0','454'),('0','630'),('2','100'),('0','600')], validators=[DataRequired()])
    pre5 = RadioField('¿Asustado Potter?',choices=[('0','No'),('0','Algo'),('0','Ya paseme profe'),('2','Ni un poco')], validators=[DataRequired()])
    
    
    submit = SubmitField("Enviar")
    
    
class consultas(FlaskForm):
    matricula=StringField('Matricula')
    grupo=StringField('Grupo')
    tipo = RadioField('¿Por que desea consultar?',
                         [validators.InputRequired(message='El campo es obligatorio.')]
                         ,choices=[('Matricula','Matricula'), ('Grupo','Grupo')])
    submit = SubmitField("Enviar")
    
        
