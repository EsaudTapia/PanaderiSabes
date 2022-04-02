from wtforms import Form,IntegerField,StringField,EmailField,FloatField,SelectField,RadioField,SubmitField,validators
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired
 
 
class RegistroCompra(FlaskForm):  
    
    
   nuevoInsummo=SubmitField("+")    
   cantidad=FloatField('cantidad', [validators.DataRequired(message='El campo es requerido')])
   precio=FloatField('Precio', [validators.DataRequired(message='El campo es requerido')])
   
   guardar = SubmitField("Guardar") 
   
   

class AddCart(FlaskForm):    

    enviar = SubmitField("+")

class Addinsumo(FlaskForm):    
    total = FloatField('Total', [validators.DataRequired(message='El campo es requerido')])
    enviar = SubmitField("Guardar")


  