from wtforms import Form,IntegerField,StringField,EmailField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired
 
 
class RegistroCompra(FlaskForm):  
    
    
   apaterno=StringField('A. paterno', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa un apellido valido')])
   amaterno=StringField('A. materno', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa un apellido valido')])
   numero=StringField('Numero', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa un grupo valido')])
   calle=StringField('Calle', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa una matricula valida')])
   colonia=StringField('Colonia', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=50, message='Ingresa un dia valido')])
   cp=IntegerField('C.P.', [validators.DataRequired(message='El campo es requerido')]
                    )
   telefono=StringField('Telefono', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=10, max=10, message='Ingresa un año valido')])
   email=EmailField('Email', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=100, message='Ingresa un año valido')])
   password=PasswordField('Contrseña', [validators.DataRequired(message='El campo es requerido'),
                                      validators.length(min=1, max=100, message='Ingresa un año valido')])
   
   comboRol= SelectField('Escoja el Rol',choices=[])
   
   guardar = SubmitField("Guardar") 
   
   



  