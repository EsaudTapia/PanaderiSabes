from flask import render_template,session,redirect,flash,url_for
from app.forms import Registro
from . import site

class Alumnos:
    def __init__(self,arch):
        self.archivo= arch
    def registro(self,matricula,nombre,apaterno,amaterno,grupo,dia,mes,año,sexo):
        a=open(self.archivo,"a")
        line ="{},{},{},{},{},{},{},{},{}\n".format(matricula,nombre,apaterno,amaterno,grupo,dia,mes,año,sexo)
        a.write(line)
        a.close()
        return True
    
    def consulta(self):
        result =[]
        ayuda = []
        a = open(self.archivo)
        for line in a:
            ayuda=line.split(",")
            result.append(ayuda)
        a.close
        return result
        

@site.route("/registros",methods=['GET','POST'])
def registros():
    return render_template("pagina1.html",)

@site.route("/nuevoalumno",methods=['GET','POST'])
def add():
    alumno_form = Registro()
    context={
        'alumno_form':alumno_form
    }
    
    if alumno_form.validate_on_submit():
        obja = Alumnos("alumnos.txt")
        resulta= obja.registro(alumno_form.matricula.data,
                               alumno_form.nombre.data,
                               alumno_form.apaterno.data,
                               alumno_form.amaterno.data,
                               alumno_form.grupo.data,
                               alumno_form.dia.data,
                               alumno_form.mes.data,
                               alumno_form.año.data,
                               alumno_form.sexo.data)
        er = 'El alumno no se pudo regitrar'
        if resulta:
            er ='Alumno regitrado'
        flash(er)
        return redirect(url_for('site.registros'))
    return render_template("pagina2.html",**context)